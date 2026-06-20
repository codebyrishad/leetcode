class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)
        
        while i < n:
            line_words = []
            current_length = 0
            
            while i < n and current_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                current_length += len(words[i])
                i += 1
            
            if i == n or len(line_words) == 1:
                left_justified = ' '.join(line_words)
                result.append(left_justified + ' ' * (maxWidth - len(left_justified)))
            else:
                total_spaces = maxWidth - current_length
                gaps = len(line_words) - 1
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = []
                for j in range(gaps):
                    line.append(line_words[j])
                    line.append(' ' * (base_spaces + (1 if j < extra_spaces else 0)))
                line.append(line_words[-1])
                result.append(''.join(line))
        
        return result