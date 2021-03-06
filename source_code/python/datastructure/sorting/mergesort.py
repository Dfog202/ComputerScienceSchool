mergesort_cnt = 0
merge_two_section_cnt = 0

def MergeTwoSection(unsorted_list, start, mid, end):
    global merge_two_section_cnt
    merge_two_section_cnt+=1
    print(start, end, "in MergeTwoSection cnt : ", merge_two_section_cnt)
    #정렬하고자 하는 리스트의 왼쪽 부분 index
    leftIdx = start
    #정렬하고자 하는 리스트의 오른쪽 부분 첫번째 idx
    rightIdx = mid + 1
    #정렬될 데이터의 수
    numOfData = (end - start) + 1
    
    #정렬된 데이터를 임시 저장할 리스트
    #데이터 개수만큼 초기화한다
    temp_list=[0 for i in range(numOfData+1)]

    #왼쪽 혹은 오른쪽 부분이 모두 temp_list에 저장되고 난 후
    #다른 쪽의 나머지를 temp_list에 담기 위한 idx
    tempIdx = 0

    #데이터의 총 개수 만큼 돌다가
    #왼쪽 부분이든 오른쪽 부분이든
    #한쪽이 모두 temp_list에 담기면 빠져나간다
    for i in range(numOfData):
        #양쪽 인덱스의 값을 비교하여 작은 수를 임시 리스트에 저장
        if unsorted_list[leftIdx] < unsorted_list[rightIdx]:
            temp_list[i] = unsorted_list[leftIdx]
            leftIdx+=1

            #leftIdx가 mid보다 커진다면
            #왼쪽 부분은 이미 모든 데이터가
            #임시 리스트에 들어간 상황
            #for문을 빠져나간다
            if leftIdx > mid:
                tempIdx = i+1
                break
        else:
            temp_list[i] = unsorted_list[rightIdx]
            rightIdx+=1

            if rightIdx > end:
                tempIdx = i + 1
                break
            

    #왼쪽 부분이 모두 임시 리스트에 올라간 상황이라면
    #오른쪽 부분의 나머지를 모두 임시 리스트에 올린다
    if leftIdx > mid:
        for i in range(rightIdx, end+1):
            temp_list[tempIdx] =unsorted_list[i]
            tempIdx+=1
    #오른쪽 부분이 모두 올라간 상황이면
    #왼쪽 부분의 나머지를 올린다
    elif rightIdx > end:
        for i in range(leftIdx, mid+1):
            temp_list[tempIdx] = unsorted_list[i]
            tempIdx+=1

    #정렬된 리스트 temp_list를
    #정렬이 안된 원본 리스트에 업데이트
    tempIdx = 0
    for i in range(start, end+1):
        unsorted_list[i] = temp_list[tempIdx]
        tempIdx+=1

    #임시 리스트는 지운다
    del temp_list

def mergesort(unsorted_list, start, end):
    #재귀함수 호출 순서를 알아보기 위한 테스트 코드
    global mergesort_cnt
    mergesort_cnt+=1
    print(start, end, "in mergesort cnt : ", mergesort_cnt)
    if start >= end:
        return

    mid = (start + end) // 2

    mergesort(unsorted_list, start, mid)
    mergesort(unsorted_list, mid+1, end)

    MergeTwoSection(unsorted_list, start, mid, end)

if __name__ == "__main__":
    unsorted = [8, 3, 7, 1, 2, 6, 4, 5]
    end = len(unsorted)-1
    mergesort(unsorted, 0, end)
    print(unsorted)

    
    

    
