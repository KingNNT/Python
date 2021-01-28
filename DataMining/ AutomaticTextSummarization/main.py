import nltk

def main():
    content = """Công sở đậm dư âm Tết trong ngày đầu làm việc.
    Trong lịch công tác của các bộ ngành 3 ngày đầu năm hầu như không có những cuộc họp. Chương trình làm việc chính của các lãnh đạo là chúc Tết. Một số nơi còn ghi lịch làm việc: lãnh đạo giải quyết công việc thường xuyên tại cơ quan. 9h sáng, hội trường Bộ Giáo dục và Đào tạo rộn tiếng cười đùa, chúc tụng, tiếng ly rượu cụng nhau chan chát. Sau đó các vụ, phòng bắt đầu những cuộc gặp gỡ riêng. Buổi "làm việc" đầu năm kết thúc sớm, với bữa tiệc tân niên tại gia. "Ngày thường, cùng cơ quan đấy nhưng mấy khi có dịp đến nhà nhau. Năm qua, người thì xây nhà mới, người thì có con đầu lòng. Đầu xuân, mọi người trong phòng đến nhà nhau, vừa chúc Tết, thăm hỏi luôn", anh Tuấn, cán bộ Tổng công ty Dệt may Việt Nam tâm sự.
    Sau 2 màn tiệc ngọt tại cơ quan, 10h sáng, các thành viên trong phòng của Tuấn "đóng cửa" bắt đầu những cuộc viếng thăm truyền thống. "Hôm nay ai có việc gấp quá thì phải làm nhưng ít người như thế lắm. Cả sếp và nhân viên công ty tôi đều đi chúc Tết. Chúc Tết các phòng xong, chúng tôi đang triệu nhau đến thăm nhà mấy người đồng nghiệp, bạn bè gần đây", chị Nguyễn Thị Bích Thư, phòng Kỹ thuật, Công ty Thép Miền Nam, 56 Thủ Khoa Huân, quận 1 (TP HCM) hoan hỷ. Rộn ràng trong công sở, không khí xuân còn tràn ngập quanh các hàng quán cà phê. 9h sáng, nhưng các hàng quán trên đường Lý Tự Trọng, quận 1 (TP HCM) vẫn khá đông công chức. Họ kể chuyện chơi Tết, chúc tụng, trao lì xì cho nhau và vui vẻ cười đùa. Anh Hoàng, cán bộ một sở trên đường Lý Tự Trọng cho biết, ngày đầu năm, lãnh đạo sở gặp mặt lãnh đạo các phòng, ban, nhân viên, ăn kẹo, uống chút bia thân mật để động viên, lấy "khí thế" làm việc cho cả năm. Dư vị Tết có lẽ phải kéo dài thêm vài ngày nữa.
    Trao đổi với VnExpress, Chánh Văn phòng của một bộ cho rằng: "Đầu năm chơi nhiều hơn làm" đã thành lệ khó sửa. Lãnh đạo cơ quan biết nhưng cũng phải thông cảm. "Anh em mời nhau đến nhà chơi, đi làm muộn một chút mình cũng phải thông cảm, quy định cứng nhắc quá thì mất vui. Tuy nhiên, công việc cơ quan vẫn phải đảm bảo", ông này nói. Cũng có một thực tế là đầu năm, người dân cũng mải vui Tết, chưa đến các cơ quan công quyền. Do vậy, không tạo áp lực công việc đối với công chức. Phòng công chứng số 1 (Hà Nội) ngày thường đông nghịt khách nhưng sáng nay vắng hoe. Anh Nguyễn Chí Thiện, công chứng viên cho biết, cả sáng chỉ có khoảng 30 hồ sơ công chứng, thấp "kỷ lục" trong năm. Vắng khách, sẵn mứt Tết "tồn đọng", nhân viên quây quần ngồi uống nước, bàn chuyện du xuân. 11h trưa, nhiều công sở ở Hà Nội khá im ắng, các quán ăn thì đông nghẹt khách. "Sáng đi được một tour rồi, trưa tụ họp ở quán ăn lấy sức. Chiều đi vài nhà nữa rồi karaoke", Ngọc Linh, nhân viên kinh doanh một hãng ôtô lớn hào hứng.
    Với nhiều công chức, ngày đầu năm đi làm còn. . vui hơn Tết!"""

    contents_parsed = content.lower() #Biến đổi hết thành chữ thường
    contents_parsed = contents_parsed.replace('\n', ' ') #Đổi các ký tự xuống dòng thành chấm câu
    contents_parsed = contents_parsed.strip() #Loại bỏ đi các khoảng trắng thừa

    sentences = nltk.sent_tokenize(contents_parsed)
    print(sentences)

if __name__ == "__main__":
    main()
