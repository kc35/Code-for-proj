def string_with_arrows(text, pos_start, pos_end):
    result = ''
  
    start = max(text.rfind('\n', 0, pos_start.idx), 0)
    end = text.find('\n', start + 1)
    if end < 0: end = len(text)
    
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calculate line columns
        line = text[start:end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)
      
        start = end
        end = text.find('\n', start + 1)
        if end < 0: end = len(text)

    return result.replace('\t', '')
