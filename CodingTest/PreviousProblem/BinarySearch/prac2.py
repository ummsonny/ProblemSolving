def binary_search(array, start, end):
    if start>end:
        return None

    mid = (start+end)//2

    #인덱스는 아무리 커져밨자 1씩 커짐(1씩 작아짐)을 생각해라! 인덱스 기준으로 생각해랏!
    if array[mid]==mid:
        return mid
    elif array[mid]<mid:
        binary_search(array, mid+1, end)
    else:
        binary_search(array, start, mid-1)