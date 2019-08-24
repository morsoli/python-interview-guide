#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 元素以一个字典储存，key是数字，value统一为1
        dic_row=[{} for i in range(9)]
        dic_col=[{} for i in range(9)]
        dic_box=[{} for i in range(9)]
        for i in range(len(board)):
            for j in range (len(board)):
                num=board[i][j]
                if num=='.':
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i][num]=1
                    dic_col[j][num]=1
                    # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                    dic_box[3*(i//3)+(j//3)][num]=1
                else:
                    return False
        return True

