import os
import subprocess
import sys

base_dir = "."

# Scripts to exclude from testing
exclude_files = {"run_tests.py", "build_kids_project.py", "build_kids_project_v2.py"}

inputs = {
    "chapter04_user_input/main.py": "Blue\n",
    "chapter04_user_input/name_greeting.py": "Alex\n",
    "chapter04_user_input/age_calculator.py": "10\n",
    "chapter04_user_input/favorite_game.py": "Minecraft\n",
    "chapter04_user_input/quiz_game.py": "10\n",
    "chapter05_conditions/game_lives.py": "2\n",
    "chapter14_exception_handling/game_input.py": "5\n",
    "chapter20_ai_basics/game_recommender.py": "yes\nno\n",
    "chapter20_ai_basics/smart_chatbot.py": "hello\nquit\n",
    "chapter21_mini_project/robot_academy.py": "Robo\nT-800\n1\n2\n3\n",
}

success = 0
failed = 0

env = os.environ.copy()
env["MPLBACKEND"] = "Agg"

for root, dirs, files in os.walk(base_dir):
    # Skip hidden directories like .github or .git
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for file in sorted(files):
        if file.endswith(".py") and file not in exclude_files:
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, base_dir)
            rel_path_posix = rel_path.replace(os.sep, '/')
            
            input_data = inputs.get(rel_path_posix, "")
            
            try:
                result = subprocess.run(
                    [sys.executable, file],
                    cwd=root,
                    input=input_data,
                    text=True,
                    capture_output=True,
                    timeout=5,
                    env=env
                )
                
                if result.returncode == 0:
                    print(f"✅ PASS: {rel_path_posix}")
                    success += 1
                else:
                    print(f"❌ FAIL: {rel_path_posix}")
                    print(f"Error output:\n{result.stderr}")
                    failed += 1
            except subprocess.TimeoutExpired:
                print(f"⏰ TIMEOUT: {rel_path_posix}")
                failed += 1
            except Exception as e:
                print(f"⚠️ ERROR running {rel_path_posix}: {e}")
                failed += 1

print(f"\nTotal Passed: {success}")
print(f"Total Failed: {failed}")
