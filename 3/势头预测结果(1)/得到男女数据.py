# import pandas as pd
#
# # 创建数据
# data = {
#     'Feature': ['server', 'serve_no', 'speed_mph', 'p2_distance_run', 'p1_distance_run', 'serve_width_score',
#                 'p1_points_won', 'p2_points_won', 'return_depth_score', 'serve_depth_score', 'rally_count',
#                 'p1_winner', 'p2_winner', 'p2_net_pt', 'p2_unf_err', 'p1_net_pt', 'p1_unf_err', 'p1_net_pt_won',
#                 'p1_break_pt', 'p1_break_pt_missed', 'p2_break_pt_missed', 'p2_net_pt_won', 'p2_break_pt',
#                 'p1_break_pt_won', 'p2_break_pt_won', 'p1_ace', 'p2_ace', 'p1_double_fault', 'p2_double_fault'],
#     'Importance': [0.786282, 0.063284, 0.021673, 0.020315, 0.019614, 0.017754, 0.016158, 0.015367, 0.009678,
#                    0.008079, 0.008052, 0.002587, 0.001716, 0.001644, 0.001600, 0.001297, 0.001171, 0.000730,
#                    0.000720, 0.000483, 0.000463, 0.000382, 0.000335, 0.000299, 0.000162, 0.000093, 0.000061,
#                    0.000000, 0.000000]
# }
#
# # 创建DataFrame
# df = pd.DataFrame(data)
#
# # 将数据写入Excel文件
# df.to_excel('feature_importance.xlsx', index=False)

#
# import pandas as pd
#
# data = {
#     'Feature': ['server', 'serve_width_score', 'speed_mph', 'serve_no', 'p2_distance_run',
#                 'p1_distance_run', 'p2_points_won', 'p1_points_won', 'return_depth_score',
#                 'rally_count', 'serve_depth_score', 'p1_winner', 'p1_net_pt', 'p2_unf_err',
#                 'p1_unf_err', 'p2_winner', 'p2_net_pt', 'p2_net_pt_won', 'p2_break_pt_missed',
#                 'p1_break_pt_missed', 'p1_net_pt_won', 'p1_break_pt', 'p2_break_pt',
#                 'p2_break_pt_won', 'p1_break_pt_won', 'p1_ace', 'p2_ace', 'p1_double_fault',
#                 'p2_double_fault'],
#     'Value': [0.757856, 0.059501, 0.031169, 0.026526, 0.020879, 0.019889, 0.017499, 0.016692,
#               0.011687, 0.008497, 0.007084, 0.004504, 0.004018, 0.002484, 0.002435, 0.002291,
#               0.001522, 0.000971, 0.000814, 0.000773, 0.000760, 0.000686, 0.000492, 0.000414,
#               0.000336, 0.000158, 0.000063, 0.000000, 0.000000]
# }
#
# df = pd.DataFrame(data)
#
# # Save to Excel
# df.to_excel('tennis_data.xlsx', index=False)










