class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digit_logs = []
        letter_logs = []
        for log in logs:
            arr = log.split()
            iden = arr[0]
            sen = ''.join(arr[1:])

            if sen.isalpha():
                letter_logs.append((iden, ' '.join(arr[1:])))
            else:
                digit_logs.append((iden, ' '.join(arr[1:])))
        
        letter_logs.sort(key=lambda x: [x[1],x[0]])

        result = letter_logs + digit_logs
        result = [' '.join(ele) for ele in result]
        return result


        