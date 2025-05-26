# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:10:18 2025

@author: cic
"""
import Stack

class website:
    def __init__(self):  
        self.Stack_array = Stack.Astack(10)  
        self.current_page = "홈"  

    def visit(self, page):
        self.Stack_array.push(self.current_page)  
        self.current_page = page
        print("현재 페이지: ",self.current_page)

    def back(self):
        if self.Stack_array.is_empty():
            print("뒤로 갈 수 없습니다")
        else:
            self.current_page = self.Stack_array.pop()
        print("현재 페이지: ",self.current_page)

    def exit(self):
        print("프로그램을 종료합니다.")

    def run(self):
        while True:
            command = input("명령어를 입력하세요: ")
            
            if command.startswith("visit "):
                page = command[6:]
                self.visit(page)

            elif command == "back":
                self.back()

            elif command == "exit":
                self.exit()
                break

            else:
                print("잘못된 명령어입니다. 다시 입력하세요.")

if __name__ == "__main__":
    tt = website()
    tt.run()