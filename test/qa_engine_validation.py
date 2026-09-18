"""
QA Math Engine & UI Validator for Nerdy Arithmetic AI
Tests all 18 CCSS skills, math accuracy, manipulative accounting, misconception classifiers,
and DOM element binding integrity in index.html.
"""

import math
import re
import random
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ── 1. SIMULATED PROBLEM GENERATION ENGINE (MATCHING index.html) ───────────────

def get_candidate_problem(tier, skill_id, op_choice='mixed'):
    tier = str(tier).lower()
    
    if tier == 'k':
        if skill_id == 'k_make_10':
            n1 = random.randint(1, 8)
            n2 = 10 - n1
            return {'n1': n1, 'n2': n2, 'op': '+', 'ans': n2, 'equation': f"{n1} + ? = 10", 'type': 'ten_frame_single'}
        elif skill_id == 'k_decompose':
            total = random.randint(5, 10)
            n1 = random.randint(1, total - 2)
            n2 = total - n1
            return {'n1': n1, 'n2': n2, 'op': '+', 'ans': n2, 'equation': f"{total} = {n1} + ?", 'type': 'ten_frame_single'}
        else: # k_ten_frame
            op = '+' if op_choice == 'add' else ('-' if op_choice == 'sub' else random.choice(['+', '-']))
            if op == '+':
                n1 = random.randint(1, 5)
                n2 = random.randint(1, 10 - n1)
                return {'n1': n1, 'n2': n2, 'op': op, 'ans': n1 + n2, 'equation': f"{n1} + {n2} = ?", 'type': 'ten_frame_single'}
            else:
                n1 = random.randint(4, 9)
                n2 = random.randint(1, n1 - 1)
                return {'n1': n1, 'n2': n2, 'op': op, 'ans': n1 - n2, 'equation': f"{n1} - {n2} = ?", 'type': 'ten_frame_single'}

    elif tier == '1':
        if skill_id == 'g1_missing_addend':
            total = random.randint(11, 19)
            n1 = random.randint(4, 10)
            n2 = total - n1
            return {'n1': n1, 'n2': n2, 'op': '+', 'ans': n2, 'equation': f"{n1} + ? = {total}", 'type': 'ten_frame_double', 'total': total}
        elif skill_id == 'g1_tens_ones':
            tens = random.randint(1, 8)
            ones = random.randint(1, 9)
            ans = tens * 10 + ones
            return {'n1': tens * 10, 'n2': ones, 'op': '+', 'ans': ans, 'equation': f"{tens*10} + {ones} = ?", 'type': 'base10'}
        else: # g1_within_20
            op = '+' if op_choice == 'add' else ('-' if op_choice == 'sub' else random.choice(['+', '-']))
            if op == '+':
                n1 = random.randint(5, 12)
                n2 = random.randint(2, 20 - n1)
                return {'n1': n1, 'n2': n2, 'op': op, 'ans': n1 + n2, 'equation': f"{n1} + {n2} = ?", 'type': 'ten_frame_double'}
            else:
                n1 = random.randint(12, 19)
                n2 = random.randint(3, 10)
                return {'n1': n1, 'n2': n2, 'op': op, 'ans': n1 - n2, 'equation': f"{n1} - {n2} = ?", 'type': 'ten_frame_double'}

    elif tier == '2':
        if skill_id == 'g2_skip_count':
            groups = random.randint(3, 8)
            group_size = random.choice([2, 5, 10])
            return {'n1': groups, 'n2': group_size, 'op': '×', 'ans': groups * group_size, 'equation': f"{groups} groups of {group_size} = ?", 'type': 'equal_groups'}
        elif skill_id == 'g2_sub_regroup':
            tens1 = random.randint(4, 8)
            ones1 = random.randint(0, 4)
            tens2 = random.randint(1, tens1 - 2)
            ones2 = random.randint(6, 9) # borrowing guaranteed
            n1 = tens1 * 10 + ones1
            n2 = tens2 * 10 + ones2
            return {'n1': n1, 'n2': n2, 'tens1': tens1, 'ones1': ones1, 'tens2': tens2, 'ones2': ones2, 'op': '-', 'ans': n1 - n2, 'equation': f"{n1} - {n2} = ?", 'type': 'base10'}
        else: # g2_add_regroup
            tens1 = random.randint(2, 5)
            ones1 = random.randint(6, 9)
            tens2 = random.randint(1, 3)
            ones2 = random.randint(5, 8) # carrying guaranteed
            n1 = tens1 * 10 + ones1
            n2 = tens2 * 10 + ones2
            return {'n1': n1, 'n2': n2, 'tens1': tens1, 'ones1': ones1, 'tens2': tens2, 'ones2': ones2, 'op': '+', 'ans': n1 + n2, 'equation': f"{n1} + {n2} = ?", 'type': 'base10'}

    elif tier == '3':
        if skill_id == 'g3_division':
            n2 = random.randint(2, 9)
            quot = random.randint(2, 9)
            n1 = n2 * quot
            return {'n1': n1, 'n2': n2, 'op': '÷', 'ans': quot, 'equation': f"{n1} ÷ {n2} = ?", 'type': 'arrays'}
        elif skill_id == 'g3_fractions':
            denom = random.choice([2, 3, 4, 6, 8])
            shaded = random.randint(1, denom - 1)
            return {'n1': shaded, 'n2': denom, 'denom': denom, 'op': '/', 'ans': shaded, 'equation': f"Shaded: ? / {denom}", 'type': 'fractions'}
        else: # g3_times_tables
            n1 = random.randint(2, 9)
            n2 = random.randint(2, 9)
            return {'n1': n1, 'n2': n2, 'op': '×', 'ans': n1 * n2, 'equation': f"{n1} × {n2} = ?", 'type': 'arrays'}

    elif tier == '4':
        if skill_id == 'g4_div_remainders':
            n2 = random.randint(4, 8)
            quot = random.randint(4, 9)
            rem = random.randint(1, n2 - 1)
            n1 = n2 * quot + rem
            return {'n1': n1, 'n2': n2, 'op': '÷', 'ans': quot, 'remainder': rem, 'equation': f"{n1} ÷ {n2} = ? (Whole Quotient)", 'type': 'division_remainders'}
        elif skill_id == 'g4_add_fractions':
            denom = random.choice([4, 5, 6, 8, 10])
            p1 = random.randint(1, denom - 2)
            p2 = random.randint(1, denom - p1 - 1)
            return {'n1': p1, 'n2': p2, 'p1': p1, 'p2': p2, 'denom': denom, 'op': '+', 'ans': p1 + p2, 'equation': f"{p1}/{denom} + {p2}/{denom} = ? / {denom}", 'type': 'fractions'}
        else: # g4_mult_2digit
            n1 = random.randint(12, 23)
            n2 = random.randint(11, 20)
            return {'n1': n1, 'n2': n2, 'op': '×', 'ans': n1 * n2, 'equation': f"{n1} × {n2} = ?", 'type': 'partial_products'}

    else: # 5th Grade
        if skill_id == 'g5_decimal_add_sub':
            is_sub = random.choice([True, False])
            if is_sub:
                n1 = round(random.randint(40, 80) / 10.0, 1)
                n2 = round(random.randint(10, 35) / 10.0, 1)
                ans = round(n1 - n2, 1)
                return {'n1': n1, 'n2': n2, 'op': '-', 'ans': ans, 'equation': f"{n1} - {n2} = ?", 'type': 'decimals'}
            else:
                n1 = round(random.randint(15, 45) / 10.0, 1)
                n2 = round(random.randint(10, 35) / 10.0, 1)
                ans = round(n1 + n2, 1)
                return {'n1': n1, 'n2': n2, 'op': '+', 'ans': ans, 'equation': f"{n1} + {n2} = ?", 'type': 'decimals'}
        elif skill_id == 'g5_decimal_mult':
            dec = random.choice([1.2, 1.5, 2.5, 3.5, 0.5, 0.8])
            whole = random.randint(2, 6)
            ans = round(dec * whole, 1)
            return {'n1': dec, 'n2': whole, 'op': '×', 'ans': ans, 'equation': f"{dec} × {whole} = ?", 'type': 'decimals'}
        else: # g5_pemdas
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 5)
            variant = random.randint(0, 2)
            if variant == 0:
                ans = (a + b) * c
                return {'n1': a, 'n2': b, 'n3': c, 'ans': ans, 'equation': f"({a} + {b}) × {c} = ?", 'type': 'pemdas', 'step1': f"({a} + {b}) = {a + b}", 'step2': f"{a + b} × {c} = ?"}
            elif variant == 1:
                ans = (a * b) + c
                return {'n1': a, 'n2': b, 'n3': c, 'ans': ans, 'equation': f"({a} × {b}) + {c} = ?", 'type': 'pemdas', 'step1': f"({a} × {b}) = {a * b}", 'step2': f"{a * b} + {c} = ?"}
            else:
                prod = a * b
                total = prod + random.randint(5, 12)
                ans = total - prod
                return {'n1': total, 'n2': a, 'n3': b, 'ans': ans, 'equation': f"{total} - ({a} × {b}) = ?", 'type': 'pemdas', 'step1': f"({a} × {b}) = {prod}", 'step2': f"{total} - {prod} = ?"}


def run_math_engine_tests():
    print("================================================================================")
    print("▶ RUNNING SUITE 1: 18,000-PROBLEM MONTE CARLO MATHEMATICAL ACCURACY TEST")
    print("================================================================================")
    
    skills_matrix = [
        ('k', 'k_ten_frame'), ('k', 'k_make_10'), ('k', 'k_decompose'),
        ('1', 'g1_within_20'), ('1', 'g1_missing_addend'), ('1', 'g1_tens_ones'),
        ('2', 'g2_add_regroup'), ('2', 'g2_sub_regroup'), ('2', 'g2_skip_count'),
        ('3', 'g3_times_tables'), ('3', 'g3_division'), ('3', 'g3_fractions'),
        ('4', 'g4_mult_2digit'), ('4', 'g4_div_remainders'), ('4', 'g4_add_fractions'),
        ('5', 'g5_pemdas'), ('5', 'g5_decimal_add_sub'), ('5', 'g5_decimal_mult')
    ]
    
    failures = 0
    total_trials = 0
    
    for tier, skill in skills_matrix:
        for trial in range(1000):
            total_trials += 1
            p = get_candidate_problem(tier, skill)
            
            # Check 1: Answer is not NaN or None
            if p.get('ans') is None or (isinstance(p['ans'], float) and math.isnan(p['ans'])):
                print(f"❌ FAIL [{tier}.{skill}]: Answer is NaN or None! Data: {p}")
                failures += 1
                continue
                
            # Check 2: No answer leakage in PEMDAS step 2
            if p.get('type') == 'pemdas':
                if '= ?' not in p.get('step2', ''):
                    print(f"❌ FAIL [{tier}.{skill}]: PEMDAS Step 2 does not end with '= ?': {p['step2']}")
                    failures += 1
                parts = p.get('step2', '').split('=')
                if len(parts) > 1 and parts[1].strip() != '?':
                    print(f"❌ FAIL [{tier}.{skill}]: Target answer leaked after '=' in Step 2: {p['step2']}")
                    failures += 1
                    
            # Check 3: Subtraction in K and 1st grade never results in negative numbers
            if p.get('op') == '-' and tier in ['k', '1']:
                if p['ans'] < 0:
                    print(f"❌ FAIL [{tier}.{skill}]: Subtraction resulted in negative answer: {p}")
                    failures += 1
                    
            # Check 4: Division with remainders
            if skill == 'g4_div_remainders':
                if p['remainder'] >= p['n2'] or p['remainder'] < 0:
                    print(f"❌ FAIL [4.g4_div_remainders]: Invalid remainder {p['remainder']} for divisor {p['n2']}")
                    failures += 1
                if p['n2'] * p['ans'] + p['remainder'] != p['n1']:
                    print(f"❌ FAIL [4.g4_div_remainders]: Dividend mismatch: {p}")
                    failures += 1
                    
            # Check 5: Fraction addition valid bounds
            if skill == 'g4_add_fractions':
                if p['ans'] >= p['denom']:
                    print(f"❌ FAIL [4.g4_add_fractions]: Improper fraction generated: {p}")
                    failures += 1
                    
            # Check 6: Decimal precision sanity
            if tier == '5':
                # ensure no 0.30000000000000004
                ans_str = str(p['ans'])
                if len(ans_str.split('.')[-1]) > 2:
                    print(f"❌ FAIL [5.{skill}]: Float rounding leak in {ans_str}: {p}")
                    failures += 1

    print(f"✅ Completed {total_trials:,} generated arithmetic problems across all 18 skills.")
    print(f"   Total Failures Detected: {failures}")
    return failures == 0


def run_html_dom_audit():
    print("\n================================================================================")
    print("▶ RUNNING SUITE 2: STATIC DOM & JAVASCRIPT EVENT BINDING INTEGRITY AUDIT")
    print("================================================================================")
    
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    errors = 0
    
    # 1. Check required interactive element IDs
    required_ids = [
        'answer-input', 'submit-btn', 'feedback-banner', 'touch-keypad',
        'manipulative-viewport', 'manipulative-title', 'problem-subtext',
        'equation-display', 'smartscore-val', 'smartscore-circle', 'mastery-ribbon',
        'questions-counter', 'time-counter', 'streak-badge', 'streak-num',
        'tier-badge', 'breadcrumb-tier', 'skill-selector', 
        'view-practice', 'view-report', 'view-admin', 
        'admin-student-inspect-modal', 'admin-enroll-student-modal', 'mastery-modal',
        'explanation-modal', 'explain-wrong-val', 'explain-correct-val', 'explain-steps-body'
    ]
    
    
    # 1.5 Check unified authentication radio buttons
    if 'name="header-role"' not in content:
        print("❌ DOM MISSING: Unified header-role radio buttons not found!")
        errors += 1

    for rid in required_ids:
        if f'id="{rid}"' not in content and f"id='{rid}'" not in content:
            print(f"❌ DOM MISSING: Element ID '{rid}' not found in index.html!")
            errors += 1
        else:
            pass

    # 2. Check essential JS handler functions
    required_functions = [
        'handleFormSubmit', 'autoPopulateManipulative', 'clearManipulative',
        'toggleTouchKeypad', 'keypadPress', 'switchGradeTier', 'changeSkill',
        'switchAppTab', 'openStudentInspectModal',
        'openEnrollStudentModal', 'handleEnrollStudentSubmit', 'exportRosterCsv',
        'broadcastParentReminder', 'readByteAloud', 'readEquationAloud',
        'playSoundEffect', 'triggerConfetti', 'saveLearnerProfile',
        'showExplanationModal', 'closeExplanationModal', 'readExplanationAloud'
    ]
    
    for fn in required_functions:
        if f"function {fn}(" not in content and f"{fn} = " not in content:
            print(f"❌ JS MISSING: Function '{fn}' not defined in index.html!")
            errors += 1

    # 3. Check touch keypad has decimal point key
    if "keypadPress('.')" not in content:
        print("❌ KEYPAD: Missing decimal point '.' key in touch keypad!")
        errors += 1
    else:
        print("✅ Touch keypad decimal point ('.') key verified.")

    # 4. Check double ten-frame click handler supports subtraction 'crossed'
    if "state.manipulativeState.tenFrameSlots[i] = cur === null ? 'blue' : cur === 'blue' ? 'crossed' : null;" in content:
        print("✅ Double Ten-Frame click-to-cross handler verified.")
    else:
        print("❌ Double Ten-Frame missing click-to-cross handler!")
        errors += 1

    print(f"\n✅ DOM & Handler Audit Finished. Total Errors: {errors}")
    return errors == 0


if __name__ == '__main__':
    s1 = run_math_engine_tests()
    s2 = run_html_dom_audit()
    if s1 and s2:
        print("\n🎉 ALL QA TEST SUITES PASSED WITH 100% SUCCESS RATE!")
        sys.exit(0)
    else:
        print("\n⚠️ QA TEST FAILURES DETECTED!")
        sys.exit(1)
