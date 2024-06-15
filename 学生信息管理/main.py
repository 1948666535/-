import csv


def main():
    students = load_students_from_file("student.txt")
    while True:
        print_menu()
        choice = input("请输入你的选择: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            query_student(students)
        elif choice == '0':
            save_students_to_file("student.txt", students)
            print("已保存学生信息并退出系统。")
            break
        else:
            print("无效选择，请重新输入。")


def print_menu():
    print("欢迎登录学生信息管理系统v1.0版本")
    print("****************************************")
    print("1、 新建学生信息")
    print("2、 显示全部学生")
    print("3、 查询学生信息")
    print("0、 保存并退出系统")
    print("****************************************")


def add_student(students):
    name = input("请输入学生姓名: ")
    phone = input("请输入学生电话: ")
    qq = input("请输入学生QQ: ")
    email = input("请输入学生电子邮箱: ")
    student = {"name": name, "phone": phone, "qq": qq, "email": email}
    students.append(student)
    print("学生信息添加成功")


def display_all_students(students):
    if not students:
        print("没有学生信息。")
        return
    for student in students:
        print(f"姓名: {student['name']}, 电话: {student['phone']}, QQ: {student['qq']}, 邮箱: {student['email']}")


def query_student(students):
    name = input("请输入要查询的学生姓名: ")
    for student in students:
        if student['name'] == name:
            print(f"姓名: {student['name']}, 电话: {student['phone']}, QQ: {student['qq']}, 邮箱: {student['email']}")
            modify_or_delete_student(student, students)
            return
    print("未找到该学生。")


def modify_or_delete_student(student, students):
    choice = input("请选择对该学生 1.修改 2.删除 0.不做任何处理 : ")
    if choice == '1':
        modify_student(student)
    elif choice== '2':
        students.remove(student)
        print("学生信息已删除。")
    elif choice == '0':
        pass
    else:
        print("无效选择。")


def modify_student(student):
    student['phone'] = input("请输入新的电话: ")
    student['qq'] = input("请输入新的QQ: ")
    student['email'] = input("请输入新的电子邮箱: ")
    print("学生信息已修改。")


def save_students_to_file(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["姓名", "电话", "QQ", "邮箱"])
        for student in students:
            writer.writerow([student['name'], student['phone'], student['qq'], student['email']])


def load_students_from_file(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # 跳过标题行
            for row in reader:
                if row:
                    student = {"name": row[0], "phone": row[1], "qq": row[2], "email": row[3]}
                    students.append(student)
    except FileNotFoundError:
        pass  # 文件不存在时不进行任何操作
    return students


if __name__ == "__main__":
    main()
