
# 显示欢迎信息
print('-'*20+'欢迎来到员工管理系统'+'-'*20)

# 创建一个列表存放员工信息
ems_list = ['冰渊\t男\t16']

# 默认信息




# 创建一个循环重复执行系统
while(True):
    # 显示选择界面
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')

    # 创建一个变量存放用户输入的内容
    user_choose = int(input('您的选择[1-4]：'))
    print('-'*60)

    # 对不同输入的输出
    if user_choose == 1 :
        # 打印表头
        print('\t序号\t姓名\t性别\t年龄')
        # 创建变量，显示员工序号
        ems_number = 1
        # 显示员工信息
        for emp in ems_list :
            print(f'\t{ems_number}\t{emp}')
            ems_number +=1
        
    elif user_choose == 2 :
        # 询问要添加员工的基本信息
        add_name = input('请输入员工姓名:')
        add_sex = input('请输入员工性别:')
        add_age = input('请输入员工年龄:')
        # 询问是否添加
        add_true_or_false = input(f'您确认要添加{add_name}员工吗[y/n]:')        
        if add_true_or_false == 'y' or add_true_or_false == 'Y' :
            # 添加
            ems_list.append(f'{add_name}\t{add_sex}\t{add_age}')
            print(f'已成功添加{add_name}员工..')
        elif add_true_or_false == 'n' or add_true_or_false == 'N' : 
            # 取消
            print('操作已取消...')
        else :
            print('请输入合法内容后再试一次...')
        
    elif user_choose == 3 :
        del_number = int(input('请输入要删除员工的序号:'))
        true_del = del_number - 1
        del_true_or_false = input(f'您确定要删除序号为{del_number}的员工吗[y/n]:')
        if del_true_or_false == 'y' or del_true_or_false == 'Y' :
            ems_list.pop(true_del)
            print(f'序号为{del_number}的员工已删除...')
        elif del_true_or_false == 'n' or del_true_or_false == 'N' :
            print('操作已取消...')
    elif user_choose == 4 :
        print('感谢您的使用.')
        input('输入回车键退出..')
        break
    else :
        print('请输入合法的数字...')
    print('-'*60)
    




