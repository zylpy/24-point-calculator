#软件说明：
#------------------------名称：24点计算器--------------------------#
#-----------------功能：计算，生成，训练24点题目-------------------#
#-----------------------代码行总数：约500行------------------------#
#-----------------适用人群：老师，学生，学习爱好者-----------------#
#-----------------使用权限：访问存储空间,生成窗口------------------#
#--使用本程序必备：python3.9+,tkinter,sys,random,threading,time库--#
#--------------------------作者：张锦轩----------------------------#
#-------------------------版本号：v4.5.0---------------------------#
from tkinter import *
from tkinter.messagebox import *
from threading import Thread as ths
import sys,time
sheching=False
#特简单计时类
class Time(object):
        def __init__(self):
                self.starttime=time.time()
                self.endtime=time.time()
        def get(self):
                self.endtime=time.time()
                return round(self.endtime-self.starttime,3)
#判断a,b,c,d是否能通过加减乘除凑成result
def tfp(a,b,c,d,result=24): #twenty four point简写
        op=('+','-','*','/')
        ns=str(a),str(b),str(c),str(d)
        for o1 in op:
                for o2 in op:
                        for o3 in op:
                                for d1,n1 in enumerate(ns):
                                        for d2,n2 in enumerate(ns):
                                                if d2==d1:
                                                        continue
                                                for d3,n3 in enumerate(ns):
                                                        if d3==d2 or d3==d1:
                                                                continue
                                                        for d4,n4 in enumerate(ns):
                                                                try:
                                                                        r=float(result)
                                                                except:
                                                                        return (False,None)
                                                                if d4==d3 or d4==d2 or d4==d1:
                                                                        continue

                                                                try:
                                                                        if eval(n1+o1+n2+o2+n3+o3+n4)==r:
                                                                                return (True,n1+o1+n2+o2+n3+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval('('+n1+o1+n2+')'+o2+n3+o3+n4)==r:
                                                                                return (True,'('+n1+o1+n2+')'+o2+n3+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval('('+n1+o1+n2+')'+o2+'('+n3+o3+n4+')')==r:
                                                                                return (True,'('+n1+o1+n2+')'+o2+'('+n3+o3+n4+')')
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval(n1+o1+n2+o2+'('+n3+o3+n4+')')==r:
                                                                                return (True,n1+o1+n2+o2+'('+n3+o3+n4+')')
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval(n1+o1+"("+n2+o2+n3+")"+o3+n4)==r:
                                                                                return (True,n1+o1+"("+n2+o2+n3+")"+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval(n1+o1+'('+n2+o2+'('+n3+o3+n4+'))')==r:                                                                      
                                                                                return (True,n1+o1+'('+n2+o2+'('+n3+o3+n4+'))')
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval(n1+o1+'(('+n2+o2+n3+')'+o3+n4+')')==r:                                                                
                                                                                return (True,n1+o1+'(('+n2+o2+n3+')'+o3+n4+')')
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval("(("+n1+o1+n2+')'+o2+n3+")"+o3+n4)==r:                                                                
                                                                                return (True,"(("+n1+o1+n2+')'+o2+n3+")"+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval('('+n1+o1+'('+n2+o2+n3+'))'+o3+n4)==r:                                                                
                                                                                return (True,'('+n1+o1+'('+n2+o2+n3+'))'+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval("("+n1+o1+n2+o2+n3+")"+o3+n4)==r:                                                                
                                                                                return (True,"("+n1+o1+n2+o2+n3+")"+o3+n4)
                                                                except:
                                                                        pass
                                                                try:
                                                                        if eval(n1+o1+'('+n2+o2+n3+o3+n4+")")==r:                                                                
                                                                                return (True,n1+o1+'('+n2+o2+n3+o3+n4+")")
                                                                except:
                                                                        pass
        return (False,None)
twp=tfp
#计算用户输入的值
def calc():
        m=twp(num1.get(),num2.get(),num3.get(),num4.get(),evalre.get())
        if m[0]:
                result.set("此题有解，解法是："+str(m[1])+"。")
        else:
                result.set("此题无解，请重新输入。")
#生成题目
def shech(mi,mx,result=24):
        global a,b,c,d
        rightan.set("")
        #检查数值有没有错误
        try:
                int(mi)
                int(mx)
                int(result)
                if int(result)< -56 or int(result)>560:
                        num2_1.set('')
                        num2_2.set('')
                        num2_3.set('')
                        num2_4.set('')
                        showerror("错误","结果取值范围应在-56 - 560")
                        return
                if int(mx)>100 or int(mx) <-20:
                        num2_1.set('')
                        num2_2.set('')
                        num2_3.set('')
                        num2_4.set('')
                        showerror("错误","数值错误(最大值取值范围应在-20 - 100内)")
                        return
                if int(mi)<-56 or int(mi)>80:
                        num2_1.set('')
                        num2_2.set('')
                        num2_3.set('')
                        num2_4.set('')
                        showerror("错误","数值错误(最小值取值范围应在-56 -80内)")
                        return 
                if int(mx)<int(mi):
                        num2_1.set('')
                        num2_2.set('')
                        num2_3.set('')
                        num2_4.set('')
                        showerror("错误","数值错误(最大值不能小于最小值)")
                        return
        except Exception as e:
                showerror("不明错误",e)
                num2_1.set('')
                num2_2.set('')
                num2_3.set('')
                num2_4.set('')
                return
        #生成题目
        from random import randint as r
        mn=int(mi)
        ma=int(mx)
        for i in range(10):
                a=r(mn,ma)
                b=r(mn,ma)
                c=r(mn,ma)
                d=r(mn,ma)
                if twp(a,b,c,d,result)[0]:
                        break
        else:
                showerror("错误","执行超时,请重新生成或更改数值")
                num2_1.set('')
                num2_2.set('')
                num2_3.set('')
                num2_4.set('')
                return 0
        num2_1.set(str(a))
        num2_2.set(str(b))
        num2_3.set(str(c))
        num2_4.set(str(d))
        return 1
#退出python程序
def exit1():
        if askyesno("确认","确认退出？"):
                sys.exit()
#显示帮助
def help1():
        showinfo("帮助","分别在四个文本框中输入数字，点击 计算 可计算题目正确答案\n第五个文本框是运算结果，默认为24\n感谢您的使用！作者：张锦轩")
#显示答案
def showan():
        global a,b,c,d
        try:
                del a,b,c,d
                rightan.set(twp(int(num2_1.get()),int(num2_2.get()),int(num2_3.get()),int(num2_4.get()),int(minre.get()))[1])
        except NameError:
                showerror("错误","答案已经显示或未点击‘生成’按钮")
        except ValueError:
                showerror("错误","答案已经显示或未点击‘生成’按钮")
#题目生成器主程序
def main():
        global num2_1,num2_2,num2_3,num2_4,rightan,minre,maxs,mins,win1
        #设置窗口
        win1=Tk()
        win1.title("题目生成器")
        win1.resizable(False,False)
        win1.geometry("400x280+480+120")
        #创建Label对象
        Label(win1,text="最小值：",font=('等线',15)).place(x=10,y=10)
        Label(win1,text="最大值：",font=('等线',15)).place(x=10,y=40)
        Label(win1,text="结果(默认为24)：",font=('等线',15)).place(x=10,y=70)
        Label(win1,text="题目：",font=('等线',15)).place(x=10,y=100)
        Label(win1,text="答案：",font=('等线',15)).place(x=10,y=130)
        #创建StringVar对象
        maxs=StringVar(win1,"1")
        mins=StringVar(win1,"10")
        minre=StringVar(win1,"24")
        rightan=StringVar(win1,"")
        num2_1=StringVar(win1,"")
        num2_2=StringVar(win1,"")
        num2_3=StringVar(win1,"")
        num2_4=StringVar(win1,"")
        #创建Entry对象
        numen1=Entry(win1,textvariable=num2_1)
        numen1.place(x=65,y=100,width=50,height=25)
        numen2=Entry(win1,textvariable=num2_2)
        numen2.place(x=110,y=100,width=50,height=25)
        numen3=Entry(win1,textvariable=num2_3)
        numen3.place(x=160,y=100,width=50,height=25)
        numen4=Entry(win1,textvariable=num2_4)
        numen4.place(x=210,y=100,width=50,height=25)
        numen1['state']="readonly"
        numen2['state']="readonly"
        numen3['state']="readonly"
        numen4['state']="readonly"
        Entry(win1,textvariable=maxs).place(x=85,y=10,height=25,width=230)
        Entry(win1,textvariable=mins).place(x=85,y=40,height=25,width=230)
        Entry(win1,textvariable=minre).place(x=165,y=70,height=25,width=150)
        ane=Entry(win1,textvariable=rightan)
        ane.place(x=65,y=130,height=25,width=330)
        ane['state']="readonly"
        #创建Button对象
        Button(win1,text="生成",command=lambda:shech(maxs.get(),mins.get(),minre.get())).place(x=325,y=15,height=75,width=70)
        Button(win1,text="显示答案",command=showan).place(x=270,y=100,height=25,width=125)
        #--------------------我是一条迷人的分割线--------------------#
        global filetra,testnum,condi
        filetra=StringVar(win1,"test.txt")
        testnum=StringVar(win1,"10")
        condi=StringVar(win1,"导出状态：空")
        Button(win1,text="导出题目",command=checkfile).place(x=330,y=180,height=60,width=60)
        Button(win1,text="帮助",command=help2,fg="yellow",bg="blue").place(x=10,y=245,height=25,width=380)
        Label(win1,text="导出数量：").place(x=10,y=180)
        Label(win1,text="导出路径：").place(x=10,y=200)
        Label(win1,textvariable=condi).place(x=10,y=220)
        Entry(win1,textvariable=testnum).place(x=70,y=182,height=20,width=250)
        Entry(win1,textvariable=filetra).place(x=70,y=202,height=20,width=250)
        win1.mainloop()
#显示题目生成器帮助
def help2():
        showinfo("帮助","\n快速生成用法：\n在 最小值 最大值 结果 中输入数字，\n点击生成按钮，即可生成题目，点击显示答案，即可显示此题目的答案。\n\n导入文件用法：\n输入导出数量，导出路径，点击导出题目，即可导出至文件\n注：最大值与最小值和结果需要在上方输入,最大值和最小值与结果取值范围分别是：\n-20到100，-56到80,-56到560,请不要超出范围,且在生成题目时不要做任何操作，直到生成完毕。\n感谢您的使用！作者：张锦轩")
#检查文件并且导出
def checkfile():
        global sheching
        if sheching:
                showwarning("警告","正在生成题目，请等待生成结束再执行操作！")
                return
        condi.set("导出状态：检查文件中")
        if askyesno("警告","如果文件存在，文件将被覆盖，确认继续？"):
                pass
        else:
                condi.set("导出状态：空")
                return
        
        try:
                file=open(filetra.get(),'w')
        except BaseException as e:
                showerror("未知错误",e)
                condi.set("导出状态：空")
                return
        #如果没问题，则关闭文件并导出
        file.close()
        condi.set("导出状态：正在导出……")
        num=int(testnum.get())
        if num>=800:
                if askyesno("警告","导出题目过多，时间可能非常长，确认继续？"):
                        pass
                else:
                        condi.set("导出状态：空")
                        return
        lists=[]
        from random import randint as r
        try:
                #生成题目
                def a():
                        global sheching
                        sheching=True
                        amax=int(maxs.get())
                        amin=int(mins.get())
                        aminre=int(minre.get())
                        file=open(filetra.get(),'w')
                        for i in range(0,num):
                                condi.set(f"导出状态：正在导出……{i}/{num}")
                                for i in range(10):
                                        fn1=r(amax,amin)
                                        fn2=r(amax,amin)
                                        fn3=r(amax,amin)
                                        fn4=r(amax,amin)
                                        if twp(fn1,fn2,fn3,fn4,aminre)[0]:
                                                break
                                else:
                                        showerror("错误","导出超时(原因可能是给定的数值无法生成题目)")
                                        condi.set("导出状态：空")
                                        return
                                lists.append(f'{fn1}  {fn2}  {fn3}  {fn4}')
                        #写入文件
                        file.write("\n".join(lists))
                        condi.set("导出状态：完成！")
                        file.close()
                        showinfo("提示",f"生成成功，{num}道24点题目")
                        condi.set("导出状态：空")
                        sheching=False
                ths(target=a).start()
                
        except BaseException as e:
                #报错并关闭文件
                showerror("未知错误",e)
                condi.set("导出状态：空")
                file.close()
#清空
def clean():
        num1.set('')
        num2.set('')
        num3.set('')
        num4.set("")
        evalre.set('24')
        result.set("请输入数字")
def th(func):
        ths(target=func).start()
#题目训练器主程序
def Cdown():
        main2_nums.set("        3")
        time.sleep(1)
        main2_nums.set("        2")
        time.sleep(1)
        main2_nums.set("        1")
        time.sleep(1)
        main2_nums.set("    开始！")
        time.sleep(1)
        teststart1()
def shechnum(smaxnum,sminnum,sresult):
        from random import randrange as r
        mn=int(sminnum)
        ma=int(smaxnum)
        while True:
                a=r(mn,ma,1)
                b=r(mn,ma,1)
                c=r(mn,ma,1)
                d=r(mn,ma,1)
                if twp(a,b,c,d,int(sresult))[0]:
                        return f"{a}  {b}  {c}  {d}"
def check():
        global win2,cdown,tmaxnum,tminnum,tresult,testatime,testtime,main2_nums,main2_result,timer
        li=main2_nums.get().split("  ")
        n1=li[0]
        n2=li[1]
        n3=li[2]
        n4=li[3]
        nums=[n1,n2,n3,n4]
        t=tresult.get()
        try:
                if eval(t)==float(main2_result.get()):
                        if n1 in t and n2 in t and n3 in t and n4 in t:
                                for i in nums:
                                        if nums.count(str(i))==li.count(str(i)):
                                                pass
                                        else:
                                                print("no")
                                                return
                                tresult.set('')
                                testatime.set(f"平均{round(float(testtime.get())/int(testnum.get()[3:]),2)}0秒钟一题")
                                main2_nums.set(shechnum(tminnum.get(),tmaxnum.get(),main2_result.get()))
                                testnum.set("题号："+str(int(testnum.get()[3:])+1))
        except Exception as e:
                return
def teststart1():
        global win2,cdown,tmaxnum,tminnum,tresult,testatime,testtime,main2_nums,main2_result,timer
        tmax=int(tmaxnum.get())
        tmin=int(tminnum.get())
        main2_nums.set(shechnum(tminnum.get(),tmaxnum.get(),main2_result.get()))
        def updatetime():

                try:
                        while True:
                                win2.state()
                                testtime.set(str(round(float(timer.get())-4,1)))
                except:
                        return
                pass
        th(updatetime)
        Label(win2,text="时间:",font=("等线",14),fg="blue").place(x=10,y=50)
        Label(win2,textvariable=testtime,font=("等线",14),fg="blue").place(x=50,y=50)
        Label(win2,textvariable=testnum,font=("等线",14),fg="orange").place(x=120,y=50)
        Label(win2,textvariable=testatime,font=("等线",14),fg="red").place(x=210,y=50)
        Label(win2,text="请在此输入答案：",font=("等线",14)).place(x=10,y=130)
        #buttons
        Button(win2,text="提交",command=check,fg="yellow",bg="blue").place(x=20,y=220,width=170,height=40)
        Button(win2,text="跳过",command=skip,fg="red",bg="orange").place(x=210,y=220,width=170,height=40)
        Entry(win2,textvariable=tresult,font=("等线",24)).place(x=20,y=160,width=360,height=50)
def skip():
        tresult.set('')
        main2_nums.set(shechnum(tminnum.get(),tmaxnum.get(),main2_result.get()))
def teststart():
        global win2,cdown,tmaxnum,tminnum,tresult,testatime,testtime,main2_nums,main2_result,timer
        main2_nums=StringVar(win2,"3")
        th(Cdown)
        Label(win2,textvariable=main2_nums,font=("等线",28),fg="red").place(x=120,y=80)
def main2():
        global win2,main2_nums,main2_result,testnum,testtime,testatime,titlevar,tmaxnum,tminnum,tresult,timer
        win2=Tk()
        win2.resizable(False,False)
        win2.geometry("400x280+100+120")
        win2.title("24点训练器")
        timer=Time()
        #hidefunc
        def hide():
                #检查数值
                try:
                        int(tmaxnum.get())
                        int(tminnum.get())
                        int(main2_result.get())
                        if int(tmaxnum.get())>int(tminnum.get()):
                                raise Exception("最大值小于最小值！")
                except Exception as e:
                        showerror("错误",str(e))
                        return
                from random import randint as r
                ma=int(tminnum.get())
                mn=int(tmaxnum.get())
                for i in range(10):
                        a=r(mn,ma)
                        b=r(mn,ma)
                        c=r(mn,ma)
                        d=r(mn,ma)
                        if twp(a,b,c,d,float(main2_result.get()))[0]:
                                break
                else:
                        showerror("错误","给定数值不能生成题目")
                        return
                
                label1.place(x=1000,y=10000)
                label2.place(x=1000,y=10000)
                label3.place(x=1000,y=10000)
                entry1.place(x=1000,y=10000)
                entry2.place(x=1000,y=10000)
                entry3.place(x=1000,y=10000)
                button1.place(x=2130,y=3418)
                button2.place(x=2130,y=3418)#不要在意乱输入的坐标
                teststart()
        #StringVar
        titlevar=StringVar(win2,"========24点训练场=======")
        main2_nums=StringVar(win2,'')
        main2_result=StringVar(win2,'')
        testnum=StringVar(win2,"题号:1")
        testtime=StringVar(win2,'0.00')
        testatime=StringVar(win2,'平均-1秒钟一题')
        tmaxnum=StringVar(win2,'1')
        tminnum=StringVar(win2,'10')
        main2_result=StringVar(win2,'24')
        tresult=StringVar(win2,'')
        #Label and Entry
        main2_title=Label(win2,textvariable=titlevar,font=('等线',18))
        main2_title.place(x=10,y=10)
        label1=Label(win2,text="最小值：",font=('等线',15))
        label1.place(x=10,y=50)
        label2=Label(win2,text="最大值：",font=('等线',15))
        label2.place(x=10,y=80)
        label3=Label(win2,text="结果(默认为24)：",font=('等线',15))
        label3.place(x=10,y=110)
        entry1=Entry(win2,textvariable=tmaxnum)
        entry1.place(x=85,y=50,height=25,width=310)
        entry2=Entry(win2,textvariable=tminnum)
        entry2.place(x=85,y=80,height=25,width=310)
        entry3=Entry(win2,textvariable=main2_result)
        entry3.place(x=165,y=110,height=25,width=230)
        #Button
        button1=Button(win2,text="开始挑战！",command=hide,bg="red",fg="yellow",font=('等线',22))
        button1.place(x=20,y=150,height=50,width=370)
        button2=Button(win2,text="帮助",command=lambda:showinfo("帮助","老样子，先设置好最大值与最小值和结果\n接着你就可以开始挑战了，在文本框中输入你的答案，点击提交\n如果没有反应，说明你答错了，要重新输入\n若实在不会，就点击跳过吧(跳过是可耻的行为，我们一定要坚持做出来！)\n温馨提示,括号要用英文括号哦,以及不要切换至计算题目界面,程序容易崩溃!\n我的成绩是平均一题15秒钟，你呢？\n祝你使用愉快！作者：张锦轩"),bg="blue",fg="yellow",font=('等线',15))
        button2.place(x=20,y=210,height=50,width=370)
        
        win2.mainloop()
#主程序
def main1():
        global num1,num2,num3,num4,result,evalre
        #创建窗口
        win=Tk()
        win.resizable(False,False)
        win.geometry("350x115+100+120")
        win.title("24点计算器")
        #创建stringvar对象
        num1=StringVar(win,"")
        num2=StringVar(win,"")
        num3=StringVar(win,"")
        num4=StringVar(win,"")
        result=StringVar(win,"请输入数字")
        evalre=StringVar(win,"24")
        #创建Entry对象
        Entry(win,textvariable=num1).place(x=10,y=10,height=25,width=45)
        Entry(win,textvariable=num2).place(x=60,y=10,height=25,width=45)
        Entry(win,textvariable=num3).place(x=110,y=10,height=25,width=45)
        Entry(win,textvariable=num4).place(x=160,y=10,height=25,width=45)
        Entry(win,textvariable=evalre).place(x=245,y=10,height=25,width=45)
        en=Entry(win,textvariable=result)
        en.place(x=10,y=45,height=25,width=280)
        Label(win,text='结果:').place(x=210,y=12)
        en["state"]="readonly"
        #创建Button对象
        Button(win,text="计算",command=calc).place(x=295,y=45,height=25,width=45)
        Button(win,text="清空",command=clean).place(x=295,y=10,height=25,width=45)
        Button(win,text="题目生成器",command=main,bg="yellow",fg="blue").place(x=240,y=80,height=25,width=100)
        Button(win,text="帮助",fg="yellow",bg="blue",command=help1).place(x=125,y=80,height=25,width=100)
        Button(win,text="24点训练器",command=main2,bg="orange",fg="red").place(x=10,y=80,height=25,width=100)
        win.mainloop()
#运行程序
if __name__ =="__main__":
        main1()

