def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):

        str1 = ""
        temp = arr1[i] | arr2[i]
        for j in range(0, n):
            if(temp & (1 << j)):
                str1 = "#" + str1
            else:
                str1 = " " + str1
        answer.append(str1)
    return answer

# ex1 = [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]]
# answer = ["#####", "# # #", "### #", "# ##", "####"]

# ex2 = [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]
# answer = ["#####", "### #", "## ##", " #### ", " #####", "### # "]
