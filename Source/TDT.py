#Selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import sys

# Khởi tạo tên đăng nhập và mật khẩu, tí đi thi về làm hàm __init__ cho ngầu


class LoginTDT:
	# Khởi tạo thuộc tính của lớp
		# Todo
	def __init__(self,username,password):
		# Todo Khởi tạo thuộc tích của đối tượng
		self.username = username
		self.password = password

	def Print(self):
		print("+ {:-<18} + {:-^15} + ".format("", ""))
		print("| {:<15} | {:>12} {:>7}".format("Các mục","Thứ tự","|"))
		print("| {:<15} | {:>10} {:>9}".format("Thông báo","1","|")) #2
		print("| {:<15} | {:>10} {:>9}".format("Học phí","2","|")) #7
		print("| {:<15} | {:>10} {:>9}".format("Thời khóa biểu","3","|")) #5
		print("| {:<15} | {:>10} {:>9}".format("Kết quả học tập","4","|")) #8
		print("| {:<15} | {:>10} {:>9}".format("Thoát","0","|")) 
		print("+ {:-<18} + {:-^15} + ".format("", ""))

	def PrintSemester(self):
		print("+ {:-<18} + {:-^15} + ".format("", ""))
		print("| {:<15} | {:>12} {:>7}".format("Học kì","Thứ tự","|"))
		print("| {:<15} | {:>10} {:>9}".format("HKI 2018-2019","1","|"))# value = 94
		print("| {:<15} | {:>10} {:>9}".format("HK2 2018-2019","2","|"))# value = 96
		print("| {:<15} | {:>10} {:>9}".format("HK hè 2018-2019","3","|"))# value = 97
		print("| {:<15} | {:>10} {:>9}".format("HKI 2019-2020","4","|"))# value = 99
		print("| {:<15} | {:>10} {:>9}".format("Thoát","0","|")) 
		print("+ {:-<18} + {:-^15} + ".format("", ""))

	def Choose(self):	
		Number_Option = int(input("{:_>28} ".format("Nhập thứ tự để chọn lựa: ")))
		if(Number_Option != 0):
			while (Number_Option<0 or Number_Option>4):
				print("Nhập số lại hoặc nhấn 0 để thoát")
				Number_Option = int(input("Nhập thứ tự để chọn: "))
				if(Number_Option == 0):
					break
		if(Number_Option == 0):
			return Number_Option	 # Trả về giá trị 0
		if(Number_Option == 1):
			return Number_Option + 1 # Trả về giá trị 2
		if(Number_Option == 2):
			return Number_Option + 5 # Trả về giá trị 7
		if(Number_Option == 3):
			return Number_Option + 2 # Trả về giá trị 5
		if(Number_Option == 4):
			return Number_Option + 4 # Trả về giá trị 8	
			
	def login(self):	

		self.Print()
		Number_Option = self.Choose()
		if(Number_Option == 0):
			sys.exit() # cái này xài tương đương với return;
			#return
			
			
		else:
			if(Number_Option == 5):
				self.PrintSemester()
				Number_Semester = self.Choose()
				if(Number_Semester == 0):
					return 
				if(Number_Semester == 2 ):
					Number_Semester = 94
				elif(Number_Semester ==7):
					Number_Semester = 96
				elif(Number_Semester ==5):
					Number_Semester = 97
				else:
					Number_Semester = 99


			driver = webdriver.Chrome("C:/Users/VanTien/Downloads/Compressed/chromedriver.exe")
			# Todo Bật wed lên cho mặc định là Chrome

			driver.get("https://student.tdt.edu.vn")
			# Todo driver la hien thi trang wed sinh viên TDT 

			driver.find_element_by_id("MSSV").send_keys(self.username)
			# Todo tim cai box ten dang nhap co id: email, sau do nhap key vao

			driver.find_element_by_id("MK").send_keys(self.password)
			# Todo tim cai box password có id:pass, sau đó send key password vào

			Login_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Đăng nhập']")[0]
			Login_button.click() # Or submit
			# Todo click button đăng nhập do không có id, path vào địa chỉ cần nhấn mở


			time.sleep(1)

			# Todo Điều hướng qua tắt thông báo
			driver.find_element_by_id("popup-thong-bao-off").click()
			# Todo Tắt thông báo khi bật Student lên

			time.sleep(1)
			# Todo làm chương trình dừng 1 giây rồi thực hiện đoạn lệnh tiếp theo

			

			# Todo Điều hướng qua mở các mục mà muốn mở #
			driver.find_elements_by_class_name('wrap-square')[Number_Option - 1].click() # Áp dụng với trường hợp chỉ có 1 class duy nhất
			#for i in range(23):
			#driver.find_elements_by_class_name('wrap-square')[9].click() # Áp dụng với trường hợp chỉ có 1 class duy nhất
			# Trường hợp driver vẫn ở trang wed mặc định khi mới tải nên tải thành công

			driver.switch_to.window(driver.window_handles[1])
			# Todo chuyển xử lí qua trang thứ 1, với trang mặc định là thứ 0


			time.sleep(5)


			if(Number_Option == 5):
				select_HK = Select(driver.find_element_by_id("ThoiKhoaBieu1_cboHocKy"))
				select_HK.select_by_value(str(Number_Semester))

				time.sleep(4)
				date_element = driver.find_elements_by_xpath("//tr[@class='Headerrow']")
				date = [x.text for x in date_element]
				print(date,"\n")

				time_element = driver.find_elements_by_xpath("//tr[@class = 'rowContent']")
				timea = [x.text for x in time_element]
				print(timea,)
				#for i in range(len(timea)):
				#	print(timea[i])
				row_content = driver.find_elements_by_xpath("//tr[@class = 'rowContent']")
				#timea = [x.text for x in time_element]

				cells = driver.find_elements_by_xpath("//td[@class ='cell' and @rowspan > '0']")
				sotiet = []
				boom = []
				sum = 0
				for i in range(len(row_content)):
				
					cell = row_content[i].find_elements_by_class_name("cell")
					

					#cell = driver.find_elements_by_xpath("//td[@class ='cell' and @rowspan > '0']")
					#boom.append(x.get_attribute("rowspan")) for x in cell]

					for x in cell:
						k = x.get_attribute("rowspan")
						boom.append(k)
						if x.text:
							sotiet.append(x.text + " Số tiết: " + k)
						else:
							sotiet.append("")

				print(boom,)

				print(sotiet,)

				



			if(Number_Option == 8):
				driver.get('https://ketquahoctap.tdt.edu.vn/Home/DiemHocKy/')
			
			print("\nDone{:->60}{:-<12}".format("Tắt hoặc dừng cmd là tắt luôn trang wed nhé",""))
			time.sleep(10800)


if __name__ == '__main__':
	Account = LoginTDT("your_username","your_password")
	Account.login()
