import os
import pandas as pd


tar_args = {
    # 筛分文件路径
    "file_path": r"文件路径",

    # 第一个筛选条件路径
    "txt_path": "",
    # 第一个筛选的列名
    "col1": "",

    "col2": "",

    # 保存文件路径
    "out": "",
}


def df_screen(data, cd_data):
    df_cy = data.copy()
    idx_z = [True for i in df_cy.index]

    def orcom(a, b): return [any([a[i], b[i]])
                             for i in range(len(a))]  # 列表a与列表b 或 比较

    def addcom(a, b): return [all([a[i], b[i]])
                              for i in range(len(a))]  # 列表a与列表b 与 比较
    for z in cd_data:
        if isinstance(cd_data[z], list):
            for index, c in enumerate(cd_data[z]):
                if index != 0:
                    idx_c = orcom(idx_c, list(df_cy[z] == c))
                else:
                    idx_c = list(df_cy[z] == c)
        else:
            idx_c = list(df_cy[z] == cd_data[z])
        idx_z = addcom(idx_z, idx_c)
    return df_cy.loc[idx_z, :]


def read_data(file_path):
    file_name = os.path.split(file_path)
    if file_name[1] == ".xlsx":
        df = pd.read_excel(file_path)
    if file_name[1] == ".csv":
        df = pd.read_csv(file_path)
    return df

def read_tar(txt_path):
    with open(txt_path, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    target = [line.strip("\n") for line in lines]
    return target

def main():
    print("开始读取数据...")
    df = read_data(tar_args["file_path"])
    df_col = [df.columns[col] for col in range(len(df.columns))]
    data_fr = pd.DataFrame(df, columns=df_col)
    target = read_tar(tar_args["txt_path"])
    for tar in range(len(target)):
        cd = {
            tar_args["col1"]: target[tar],
            tar_args["col2"]: [],
        }
        new_df = df_screen(data_fr, cd)
        try:
            new_df.to_excel(tar_args["out"] + "/" + str(target[tar]) + '.xlsx', index=False, encoding="gbk")
            print(f"{str(tar+1)} {str(target[tar])} .xlsx is saved.")
        except:
            new_df.to_csv(tar_args["out"] + "/" + str(target[tar]) + '.csv', index=False, encoding="utf-8")
            print(f"{str(tar+1)} {str(target[tar])} .csv is saved.")
        else:
            pass
    print("over")

if __name__ == "__main__":
    main()
    