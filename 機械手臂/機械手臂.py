#Magician
current_pose = dType.GetPose(api) #�bMOVL�Ҧ��U�B��PTP�R�O�A�N���u���ʨ�Ѽƫ��w����m�C
dType.SetPTPCmdEx(api, 2, 148,  193,  15, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 148,  193,  (-4.3), current_pose[3], 1)
#def SetEndEffectorParamsEx(api, xBias, yBias, zBias, isQueued=0)
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1) #�ھ��u�y����(SuctionCup)�������]�m������
dType.SetEndEffectorSuctionCupEx(api, 1, 1) #����l�L{ON, OFF}�����A
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 148,  193,  15, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 134,  0,  15, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 134,  0,  (-4.799), current_pose[3], 1)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 134,  0,  15, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 148,  193,  15, current_pose[3], 1)