import tkinter as tk

class ExtractZIP(tk.Tk):
    zipFiles = tuple()

    def __init__(self):
        super().__init__()
        self.title(" Extract Zip FIles! ")
        self.geometry("400x250+50+50")
        self.iconbitmap('./.ico/me.ico')

        text = tk.Label(self, text="\n이 프로그램은 여러 개의 Zip파일을 \n동시에 해제해주는 프로그램입니다.\n")
        btn1 = tk.Button(self, text="Zip 파일(.zip)  선택", command=self.get_zip, width=30)
        btn2 = tk.Button(self, text="실행하기", command=self.start_extract, width=30, height=2)
        text2 = tk.Label(self, text="\n만든 사람 : https://github.com/mb5ss95", height=2)

        text.pack(pady="10")
        btn1.pack(side="top", pady="5")
        btn2.pack(side="top", pady="5")
        text2.pack(side="top", pady="10")

    def get_zip(self):
        from tkinter.filedialog import askopenfilenames
        from tkinter import messagebox
        

        self.zipFiles = askopenfilenames(title='압축 해제할 파일을 선택하세요.', filetypes=[('압축 파일 (.zip)', '*.zip')])

        if len(self.zipFiles) == 0:
            messagebox.showerror(    "메시지 알림", "  취소하셨습니다!")
        else:
            messagebox.showinfo(title="선택한 Zip 파일", message=f" {len(self.zipFiles)}개 선택됨\n")
        
    def start_extract(self):
        import os
        from tkinter import messagebox
        import zipfile

        if len(self.zipFiles) == 0:
            messagebox.showerror(    "메시지 알림", "  파일을 선택하세요!")
            return
        
        path = os.path.dirname(self.zipFiles[0])
        print(path)

        for i in self.zipFiles:
            zipfile.ZipFile(i).extractall(path=path+"/result")
        
        messagebox.showinfo(title="완료!!!", message="모두 완료 되었습니다!")
        self.destroy()


if __name__ == '__main__':
    import tkinter as tk
    
    extractZip = ExtractZIP()
    extractZip.mainloop()

