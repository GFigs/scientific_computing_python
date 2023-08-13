def arithmetic_arranger(problems, display_answers=False):

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  if len(problems) > 5:
    return "Error: Too many problems"

  for problem in problems:
    parts = problem.split()
    operators = ["+", "-"]
    operand1 = parts[0] 
    operator = parts[1]
    operand2 = parts[2]
    
    if operator not in operators:
      return "Error: Operator must be '+' or '-'."

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(operand1), len(operand2) + 2)

    line1 = line1 + operand1.rjust(width) + "    "
    line2 = line2 + operator + " "+ operand2.rjust(width - 2) + "    "
    line3 = line3 + "-" * (width) + "    "

    if display_answers:
      if operator == "+":
        result = str(int(operand1) + int(operand2))
      else:
        result = str(int(operand1) - int(operand2))

      line4 = line4 + result.rjust(width) + "    "

  if display_answers:
    arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
  else:
    arranged_problems = f"{line1}\n{line2}\n{line3}"
    
  return arranged_problems