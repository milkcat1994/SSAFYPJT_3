import FaceController
import cv2

# img = cv2.imread("samples/friends/seulgi_1.jpg")
img = cv2.imread("samples/friends/redvelvet1.jpg")
# img = cv2.imread("samples/friends/test.jpg")
friends = [
    {'kid':0, 'fname':'슬기', 'img_url':'samples/friends/seulgi_org_1.jpg'},
    {'kid':0, 'fname':'슬기', 'img_url':'samples/friends/seulgi_org_2.jpg'}
]


# 인자값
'''
img : 원본 이미지
friends : 사용자의 친구 리스트

리턴값
list : 얼굴만 crop된 사각형 좌표
faces_crop : 얼굴만 crop된 이미지들
friend_list :
{
  'fname': '이름',
  'square': 사각형좌표,
  'idx':list의 해당 image index
}
'''
list, faces_crop, friend_list = FaceController.face_detection(img, friends)

print(list)
print(len(faces_crop))
print(friend_list)



# 인자값
'''
option_type : 'blur' => 블러, 'fixel' => 픽셀, 'face' => 가상얼굴, 'sticker' => 스티커
img : 원본 이미지
swap_area : 수정할 사각형 좌표
option_level : (1~5)

리턴값
img : 수정된 이미지
'''
# img = FaceController.face_transform(option_type, img, swap_area, option_level)

# print(list)

# 스티커
'''
img : 원본이미지
swap_area : 수정할 사각형 좌표
sticker : 스티커이미지

리턴값
img : 수정된 이미지
'''
#img = FaceController.sticker_swap(img, chage_area, sticker)
