import pandas as pd


class Example():
    # example to test Power BI integration
    def do_it(self):
        data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
        df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
        print(df)


if __name__ == '__main__':
    e = Example()
    e.do_it()
