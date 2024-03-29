from typing import List


def parse_experssion(s: str) -> List[str]:
    """
    過濾字串s空格，並分割數字、運算子，儲存成list
    輸入： s = "15 * ( 2+31)"
    輸出： exp = ['15', '*', '(', '2', '+', '31', ')']
    """
    exp = []

    for c in s:
        if c == " ":
            continue
        elif c.isdigit() and exp and exp[-1].isdigit():  # 如果前一個元素是數字，直接加到後方
            exp[-1] += c
        else:
            exp.append(c)

    return exp


def inorder_to_postorder(inorder: List[str]) -> List[str]:
    """
    中序式轉後序式
    輸入： inorder = ['15', '*', '(', '2', '+', '31', ')']
    輸出： postorder = ['15', '2', '31', '+', '*']
    """
    priority = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0,
        ")": 0
    }

    postorder = []
    st = []  # 只存運算子

    for c in inorder:
        if c.isdigit():  # 數字直接輸出
            postorder.append(c)
        elif c == "(":  # 左括號直接入堆疊，之後搭配右括號使用
            st.append("(")
        elif c == ")":  # 將左右括號範圍內的東西全部輸出
            while st[-1] != "(":
                postorder.append(st.pop())
            st.pop()
        else:  # 將優先度高於等於當前運算子c的運算子全部輸出，最後才將c入堆疊
            while st and priority[c] <= priority[st[-1]]:
                postorder.append(st.pop())
            st.append(c)

    while st:  # 剩餘堆疊全部輸出
        postorder += st.pop()

    return postorder


def calculate_postorder(postorder: List[str]) -> int:
    """
    計算後序式結果
    輸入： postorder = ['15', '2', '31', '+', '*']
    輸出： sum = 495
    """
    st = []

    for c in postorder:
        if c.isdigit():
            st.append(int(c))
            continue
        b = st.pop()
        a = st.pop()
        if c == "+":
            st.append(a+b)
        elif c == "-":
            st.append(a-b)
        elif c == "*":
            st.append(a*b)
        elif c == "/":
            st.append(int(a/b))  # 向0取整

    return sum(st)


s = "15 * ( 2+31)"
print(s)
IN = parse_experssion(s)
print(IN)
POST = inorder_to_postorder(IN)
print(POST)
RES = calculate_postorder(POST)
print(RES)  # 495
