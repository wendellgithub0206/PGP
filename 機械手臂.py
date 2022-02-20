#Magician
current_pose = dType.GetPose(api) #在MOVL模式下運行PTP命令，將手臂移動到參數指定的位置。
dType.SetPTPCmdEx(api, 2, 148,  193,  15, current_pose[3], 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 148,  193,  (-4.3), current_pose[3], 1)
#def SetEndEffectorParamsEx(api, xBias, yBias, zBias, isQueued=0)
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1) #根據臂尖附件(SuctionCup)的類型設置偏移值
dType.SetEndEffectorSuctionCupEx(api, 1, 1) #控制吸盤{ON, OFF}的狀態
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