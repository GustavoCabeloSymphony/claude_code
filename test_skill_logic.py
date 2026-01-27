#!/usr/bin/env python3
"""
Test script for Claude Code skill logic validation.

This script tests whether skill outputs (like the 'explaining-code' skill)
meet their required criteria.
"""

import re
import sys
from typing import Dict


class SkillTester:
    """Tests skill outputs against defined requirements."""

    def __init__(self):
        self.results = []

    def test_explaining_code_skill(self, explanation: str) -> Dict[str, any]:
        """
        Test the 'explaining-code' skill output.

        Required elements:
        1. Start with an analogy
        2. Draw a diagram (ASCII art)
        3. Walk through the code
        4. Highlight a gotcha

        Args:
            explanation: The skill output text to validate

        Returns:
            Dict with test results and feedback
        """
        results = {
            'passed': True,
            'checks': {},
            'score': 0,
            'max_score': 4
        }

        # Check 1: Contains an analogy
        has_analogy = self._check_analogy(explanation)
        results['checks']['analogy'] = {
            'passed': has_analogy,
            'description': 'Contains an analogy or comparison'
        }
        if has_analogy:
            results['score'] += 1

        # Check 2: Contains a diagram (ASCII art)
        has_diagram = self._check_diagram(explanation)
        results['checks']['diagram'] = {
            'passed': has_diagram,
            'description': 'Contains ASCII diagram or visual representation'
        }
        if has_diagram:
            results['score'] += 1

        # Check 3: Contains code walkthrough
        has_walkthrough = self._check_walkthrough(explanation)
        results['checks']['walkthrough'] = {
            'passed': has_walkthrough,
            'description': 'Includes step-by-step code explanation'
        }
        if has_walkthrough:
            results['score'] += 1

        # Check 4: Highlights a gotcha
        has_gotcha = self._check_gotcha(explanation)
        results['checks']['gotcha'] = {
            'passed': has_gotcha,
            'description': 'Mentions common mistakes or misconceptions'
        }
        if has_gotcha:
            results['score'] += 1

        results['passed'] = results['score'] == results['max_score']

        return results

    def _check_analogy(self, text: str) -> bool:
        """Check if text contains an analogy or comparison."""
        analogy_patterns = [
            r'\blike\s+(?:a|an)\b',
            r'\bsimilar\s+to\b',
            r'\bcompare\s+(?:to|with)\b',
            r'\bimagine\b',
            r'\bthink\s+of\s+(?:it|this)\s+as\b',
            r'\bjust\s+as\b',
            r'\bin\s+the\s+same\s+way\b',
            r'\banalog(?:y|ous)\b'
        ]
        return any(re.search(pattern, text, re.IGNORECASE) for pattern in analogy_patterns)

    def _check_diagram(self, text: str) -> bool:
        """Check if text contains ASCII art or diagram."""
        # Look for common ASCII diagram patterns
        diagram_indicators = [
            r'[+\-|]{3,}',  # Box drawing characters
            r'[─│┌┐└┘├┤┬┴┼]',  # Unicode box drawing
            r'[→←↑↓⟶⟵]',  # Arrows
            r'^\s*[|/\\]',  # Visual connectors at start of line
            r'\[.*\].*[→←]',  # Boxes with arrows
        ]

        # Check for multiple lines with ASCII art characters
        lines = text.split('\n')
        ascii_lines = 0
        for line in lines:
            # Check for box drawing or arrows
            if any(re.search(pattern, line) for pattern in diagram_indicators):
                ascii_lines += 1
            # Also check for bracket-based diagrams
            elif re.search(r'[├└│]', line) or (line.count('[') >= 2 and line.count(']') >= 2):
                ascii_lines += 1

        return ascii_lines >= 2  # At least 2 lines with diagram elements

    def _check_walkthrough(self, text: str) -> bool:
        """Check if text contains a step-by-step explanation."""
        walkthrough_patterns = [
            r'\b(?:first|second|third|then|next|finally|step\s*\d+)\b',
            r'\d+\.\s+\w+',  # Numbered list
            r'(?:^|\n)\s*-\s+\w+',  # Bulleted list
            r'\bwhen\s+\w+.*,\s*(?:it|the)',  # Conditional explanation
            r'\bafter\s+(?:that|this)\b',
        ]

        matches = sum(1 for pattern in walkthrough_patterns
                     if re.search(pattern, text, re.IGNORECASE | re.MULTILINE))

        return matches >= 2  # At least 2 walkthrough indicators

    def _check_gotcha(self, text: str) -> bool:
        """Check if text highlights gotchas or common mistakes."""
        gotcha_patterns = [
            r'\bgotcha\b',
            r'\bcommon\s+(?:mistake|error|pitfall|misconception)\b',
            r'\bwatch\s+out\b',
            r'\bbe\s+careful\b',
            r'\bnote\s+that\b',
            r'\bimportant(?:ly)?\b',
            r'\bmight\s+(?:think|expect|assume)\b',
            r'\bdon\'t\s+(?:forget|confuse)\b',
            r'\beasy\s+to\s+(?:miss|forget|overlook)\b',
            r'\bcatch\b.*\bwas\b',
        ]
        return any(re.search(pattern, text, re.IGNORECASE) for pattern in gotcha_patterns)

    def print_results(self, results: Dict) -> None:
        """Pretty print test results."""
        print("\n" + "="*60)
        print("SKILL LOGIC TEST RESULTS")
        print("="*60)
        print(f"\nOverall Status: {'✓ PASSED' if results['passed'] else '✗ FAILED'}")
        print(f"Score: {results['score']}/{results['max_score']}")
        print("\nDetailed Checks:")
        print("-"*60)

        for check_name, check_data in results['checks'].items():
            status = "✓" if check_data['passed'] else "✗"
            print(f"{status} {check_name.capitalize()}: {check_data['description']}")

        print("\n" + "="*60)


def test_sample_explanations():
    """Run tests on sample explanations."""
    tester = SkillTester()

    # Sample 1: Good explanation
    good_explanation = """
    Think of this function like a recipe book. Each recipe (function) has a list of
    ingredients (parameters) and steps to follow.

    Here's the flow:
    ```
    Input → [Process] → Output
              ↓
         [Validation]
    ```

    Let me walk through it:
    1. First, we receive the input
    2. Then we validate it
    3. Finally, we process and return the result

    Common mistake: Forgetting to validate the input can lead to errors downstream.
    """

    # Sample 2: Missing diagram
    missing_diagram = """
    This is like a traffic light controlling the flow. First, it checks the condition,
    then it proceeds. Step 1 happens first, then step 2. Watch out for null values!
    """

    # Sample 3: Missing gotcha
    missing_gotcha = """
    Think of this like a filing cabinet. Here's the structure:
    ```
    [Cabinet]
      ├── [Drawer 1]
      └── [Drawer 2]
    ```
    First, we open the cabinet. Then we find the right drawer. Finally, we retrieve the file.
    """

    print("\n" + "="*60)
    print("TESTING SKILL LOGIC VALIDATOR")
    print("="*60)

    print("\n### Test 1: Complete Explanation (Should PASS)")
    results1 = tester.test_explaining_code_skill(good_explanation)
    tester.print_results(results1)

    print("\n### Test 2: Missing Diagram (Should FAIL)")
    results2 = tester.test_explaining_code_skill(missing_diagram)
    tester.print_results(results2)

    print("\n### Test 3: Missing Gotcha (Should FAIL)")
    results3 = tester.test_explaining_code_skill(missing_gotcha)
    tester.print_results(results3)


def test_custom_explanation(explanation_text: str):
    """Test a custom explanation provided by the user."""
    tester = SkillTester()
    results = tester.test_explaining_code_skill(explanation_text)
    tester.print_results(results)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        # Read explanation from file
        if len(sys.argv) < 3:
            print("Usage: python test_skill_logic.py --file <filename>")
            sys.exit(1)

        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            explanation = f.read()

        print(f"\nTesting explanation from: {sys.argv[2]}")
        test_custom_explanation(explanation)

    elif len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        # Interactive mode
        print("Enter your explanation (press Ctrl+D when done):")
        explanation = sys.stdin.read()
        test_custom_explanation(explanation)

    else:
        # Run sample tests
        test_sample_explanations()

        print("\n" + "="*60)
        print("USAGE")
        print("="*60)
        print("\nTo test your own explanations:")
        print("  python test_skill_logic.py --file <explanation.txt>")
        print("  python test_skill_logic.py --interactive")
        print("\nTo run sample tests:")
        print("  python test_skill_logic.py")
        print()
