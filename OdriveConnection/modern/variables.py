# jlist = [
#     'K4ABT_JOINT_PELVIS',
#     'K4ABT_JOINT_SPINE_NAVEL',
#     'K4ABT_JOINT_SPINE_CHEST',
#     'K4ABT_JOINT_NECK',
#     'K4ABT_JOINT_CLAVICLE_LEFT',
#     'K4ABT_JOINT_SHOULDER_LEFT',
#     'K4ABT_JOINT_ELBOW_LEFT',
#     'K4ABT_JOINT_WRIST_LEFT',
#     'K4ABT_JOINT_HAND_LEFT',
#     'K4ABT_JOINT_HANDTIP_LEFT',
#     'K4ABT_JOINT_THUMB_LEFT',
#     'K4ABT_JOINT_CLAVICLE_RIGHT',
#     'K4ABT_JOINT_SHOULDER_RIGHT',
#     'K4ABT_JOINT_ELBOW_RIGHT',
#     'K4ABT_JOINT_WRIST_RIGHT',
#     'K4ABT_JOINT_HAND_RIGHT',
#     'K4ABT_JOINT_HANDTIP_RIGHT',
#     'K4ABT_JOINT_THUMB_RIGHT',
#     'K4ABT_JOINT_HIP_LEFT',
#     'K4ABT_JOINT_KNEE_LEFT',
#     'K4ABT_JOINT_ANKLE_LEFT',
#     'K4ABT_JOINT_FOOT_LEFT',
#     'K4ABT_JOINT_HIP_RIGHT',
#     'K4ABT_JOINT_KNEE_RIGHT',
#     'K4ABT_JOINT_ANKLE_RIGHT',
#     'K4ABT_JOINT_FOOT_RIGHT',
#     'K4ABT_JOINT_HEAD',
#     'K4ABT_JOINT_NOSE',
#     'K4ABT_JOINT_EYE_LEFT']
#
#
#
# # for i in range(29):
# #     x = 12
# #     print(jlist[i][x:] + "x =",f"close_body.joints[{i}].position.xyz.x")
# #     print(jlist[i][x:] + "y =",f"close_body.joints[{i}].position.xyz.y")
# #     print(jlist[i][x:] + "z =",f"close_body.joints[{i}].position.xyz.z")
#
# print('global' ,end = " ")
# for i in range(29):
#     x = jlist[i][12:] + "x,"
#     y = jlist[i][12:] + "y,"
#     z = jlist[i][12:] + "z,"
#     print(x.lower(), end=" ")
#     print(y.lower(), end=" ")
#     print(z.lower(), end=" ")
#
#
#
# '''
# pelvisx = close_body.joints[0].position.xyz.x
# pelvisy = close_body.joints[0].position.xyz.y
# pelvisz = close_body.joints[0].position.xyz.z
# spine_navelx = close_body.joints[1].position.xyz.x
# spine_navely = close_body.joints[1].position.xyz.y
# spine_navelz = close_body.joints[1].position.xyz.z
# spine_chestx = close_body.joints[2].position.xyz.x
# spine_chesty = close_body.joints[2].position.xyz.y
# spine_chestz = close_body.joints[2].position.xyz.z
# neckx = close_body.joints[3].position.xyz.x
# necky = close_body.joints[3].position.xyz.y
# neckz = close_body.joints[3].position.xyz.z
# clavicle_leftx = close_body.joints[4].position.xyz.x
# clavicle_lefty = close_body.joints[4].position.xyz.y
# clavicle_leftz = close_body.joints[4].position.xyz.z
# shoulder_leftx = close_body.joints[5].position.xyz.x
# shoulder_lefty = close_body.joints[5].position.xyz.y
# shoulder_leftz = close_body.joints[5].position.xyz.z
# elbow_leftx = close_body.joints[6].position.xyz.x
# elbow_lefty = close_body.joints[6].position.xyz.y
# elbow_leftz = close_body.joints[6].position.xyz.z
# wrist_leftx = close_body.joints[7].position.xyz.x
# wrist_lefty = close_body.joints[7].position.xyz.y
# wrist_leftz = close_body.joints[7].position.xyz.z
# hand_leftx = close_body.joints[8].position.xyz.x
# hand_lefty = close_body.joints[8].position.xyz.y
# hand_leftz = close_body.joints[8].position.xyz.z
# handtip_leftx = close_body.joints[9].position.xyz.x
# handtip_lefty = close_body.joints[9].position.xyz.y
# handtip_leftz = close_body.joints[9].position.xyz.z
# thumb_leftx = close_body.joints[10].position.xyz.x
# thumb_lefty = close_body.joints[10].position.xyz.y
# thumb_leftz = close_body.joints[10].position.xyz.z
# clavicle_rightx = close_body.joints[11].position.xyz.x
# clavicle_righty = close_body.joints[11].position.xyz.y
# clavicle_rightz = close_body.joints[11].position.xyz.z
# shoulder_rightx = close_body.joints[12].position.xyz.x
# shoulder_righty = close_body.joints[12].position.xyz.y
# shoulder_rightz = close_body.joints[12].position.xyz.z
# elbow_rightx = close_body.joints[13].position.xyz.x
# elbow_righty = close_body.joints[13].position.xyz.y
# elbow_rightz = close_body.joints[13].position.xyz.z
# wrist_rightx = close_body.joints[14].position.xyz.x
# wrist_righty = close_body.joints[14].position.xyz.y
# wrist_rightz = close_body.joints[14].position.xyz.z
# hand_rightx = close_body.joints[15].position.xyz.x
# hand_righty = close_body.joints[15].position.xyz.y
# hand_rightz = close_body.joints[15].position.xyz.z
# handtip_rightx = close_body.joints[16].position.xyz.x
# handtip_righty = close_body.joints[16].position.xyz.y
# handtip_rightz = close_body.joints[16].position.xyz.z
# thumb_rightx = close_body.joints[17].position.xyz.x
# thumb_righty = close_body.joints[17].position.xyz.y
# thumb_rightz = close_body.joints[17].position.xyz.z
# hip_leftx = close_body.joints[18].position.xyz.x
# hip_lefty = close_body.joints[18].position.xyz.y
# hip_leftz = close_body.joints[18].position.xyz.z
# knee_leftx = close_body.joints[19].position.xyz.x
# knee_lefty = close_body.joints[19].position.xyz.y
# knee_leftz = close_body.joints[19].position.xyz.z
# ankle_leftx = close_body.joints[20].position.xyz.x
# ankle_lefty = close_body.joints[20].position.xyz.y
# ankle_leftz = close_body.joints[20].position.xyz.z
# foot_leftx = close_body.joints[21].position.xyz.x
# foot_lefty = close_body.joints[21].position.xyz.y
# foot_leftz = close_body.joints[21].position.xyz.z
# hip_rightx = close_body.joints[22].position.xyz.x
# hip_righty = close_body.joints[22].position.xyz.y
# hip_rightz = close_body.joints[22].position.xyz.z
# knee_rightx = close_body.joints[23].position.xyz.x
# knee_righty = close_body.joints[23].position.xyz.y
# knee_rightz = close_body.joints[23].position.xyz.z
# ankle_rightx = close_body.joints[24].position.xyz.x
# ankle_righty = close_body.joints[24].position.xyz.y
# ankle_rightz = close_body.joints[24].position.xyz.z
# foot_rightx = close_body.joints[25].position.xyz.x
# foot_righty = close_body.joints[25].position.xyz.y
# foot_rightz = close_body.joints[25].position.xyz.z
# headx = close_body.joints[26].position.xyz.x
# heady = close_body.joints[26].position.xyz.y
# headz = close_body.joints[26].position.xyz.z
# nosex = close_body.joints[27].position.xyz.x
# nosey = close_body.joints[27].position.xyz.y
# nosez = close_body.joints[27].position.xyz.z
# eye_leftx = close_body.joints[28].position.xyz.x
# eye_lefty = close_body.joints[28].position.xyz.y
# eye_leftz = close_body.joints[28].position.xyz.z
#
# '''

# importing package
from better_profanity import profanity
profanity.load_censor_words()
