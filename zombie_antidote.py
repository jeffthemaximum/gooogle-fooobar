import operator

# def is_unique(meeting, meetings, uniques):

#     # 1
#     if meeting in uniques:
#         return False

#     meetings_without_meeting = meetings[:]
#     meetings_without_meeting.remove(meeting)
#     for i in range(len(meetings_without_meeting)):

#         # check bigger
#         if meeting[0] < meetings_without_meeting[i][0] and meeting[1] > meetings_without_meeting[i][1]:
#             return False
#         # else check smaller
#         if meeting[0] > meetings_without_meeting[i][0] and meeting[1] < meetings_without_meeting[i][1]:
#             return False
#         # else check starttime overlap
#         elif meeting[0] < meetings_without_meeting[i][1] and meeting[1] > meetings_without_meeting[i][0]:
#             return False
#         # else check endtime overlap
#         elif meeting[1] > meetings_without_meeting[i][0] and meeting[0] < meetings_without_meeting[i][1]:
#             return False
#         # else check length of zero
#         elif len(meetings_without_meeting) == 0:
#             return False
#     else:
#         return True

def checker(meeting, sorted_meetings, uniques):
    for unique in uniques:
        if meeting[0] < unique[1]:
            if meeting[1] > unique[0]:
                return True
    return False

def answer(meetings):
    uniques = []
    sorted_meetings = sorted(meetings, key=operator.itemgetter(1))
    for meeting in sorted_meetings:
        check = checker(meeting, sorted_meetings, uniques)
        if check is False:
            uniques.append(meeting)
    
    print len(uniques)

answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5], [2, 6]])