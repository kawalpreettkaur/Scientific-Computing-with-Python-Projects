def arithmetic_arranger(problems,answer=False):
  operators = ['+','-']
  arranged_problems = ''''''
  dashes=[]
  space = ' '
  answers = []

  # problems limit is five
  if len(problems) > 5:
    return "Error: Too many problems."

  # entering into each problem to perform actions
  for problem_set in problems:

    # space seperator for each problem
    if problem_set != problems[0]:
      arranged_problems+=space*4

    # breaks the str into a list, containing digits & an operator in mid pos
    values = problem_set.split()
    
    # appropriate operators are addition and subtraction
    if values[1] not in operators :
      return "Error: Operator must be '+' or '-'."
    
    # operands must be four digits in width
    if len(values[0]) > 4 or len(values[2]) >4 :
      return "Error: Numbers cannot be more than four digits."

    # operands must be digits
    if values[0].isdigit() == False or values[2].isdigit() == False:
        return "Error: Numbers must only contain digits."


    # Sample format
    #          values[0]
    #values[1] values[2]
    #-------------------

    # Breaking down into top & bottom row

    # Arrangement for given top row for each Problem
      
    # Gets the length to place digits accordingly
    top_length = len(values[0])
    bottom_length = len(values[2])

    # Gets the maximum & minimum length digit
    maxLength = max(top_length,bottom_length)
    minLength = min(top_length,bottom_length)
    

    # answer generation when second argument is given
    if answer == True:
      # eval helps in performing calculation on str as int & str as operators
      result = eval(f'{values[0]} {values[1]} {values[2]}')
      
      result_width = len(str(result))
      # adding spaces accordig to result's width in respective list
      answer_spaces = maxLength+2 - result_width
      answers.append(space*answer_spaces)
      answers.append(result)
      # space seperator after every result
      if problem_set!= problems[-1]:
        answers.append(space*4)
      print(answers)

    # Total spaces for top number
    # Add +2 for operator's position and a space after operator
    top_spaces = 2
    if bottom_length > top_length: 
      top_spaces += maxLength - minLength 
    space = ' '

    arranged_problems += f'{space*top_spaces}{values[0]}'

  arranged_problems +='\n'

  # Arrangement for given bottom row for each Problem
  for problem_set in problems:
    if problem_set != problems[0]:
      arranged_problems+=space*4
    values = problem_set.split()
    

    # Arrangement for given bottom row for each Problem
    top_length = len(values[0])
    bottom_length = len(values[2])
    maxLength = max(top_length,bottom_length)
    minLength = min(top_length,bottom_length)

    
    bottom_spaces=1
    if top_length > bottom_length: 
      bottom_spaces+= top_length - bottom_length 
    space = ' '
    dash='-'
    dashes.append(dash*(maxLength+2))
    if problem_set != problems[-1]:
      
      dashes.append(space*4)
    arranged_problems += f'{values[1]}{space*bottom_spaces}{values[2]}'
  arranged_problems +='\n'

  # adding dashes
  for _ in dashes:
    arranged_problems += f'{_}'

  # generating answer
  if answer == True:
    arranged_problems += '\n'  
  for sol in answers:
   
    arranged_problems += f'{sol}'
  
  
  return arranged_problems
