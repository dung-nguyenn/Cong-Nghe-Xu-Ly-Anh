<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Logo_DAI_NAM.png/400px-Logo_DAI_NAM.png" alt="Đại học Đại Nam Logo" width="150"/>
  
  <h3>TRƯỜNG ĐẠI HỌC ĐẠI NAM</h3>
  <h4>KHOA CÔNG NGHỆ THÔNG TIN - CHUYÊN NGÀNH AI & IoT</h4>
  
  <br>

  # Hệ Thống Nhận Diện Bệnh Trên Lá Lúa Sử Dụng CNN
  
  <p>
    Dự án nghiên cứu và phát triển mô hình nhận diện, phân loại các loại bệnh trên lá lúa thông qua phân tích hình ảnh sử dụng Mạng nơ-ron tích chập (CNN) với Keras và TensorFlow.
  </p>
</div>

---

## 📖 Giới thiệu đề tài

**Nhận Diện Bệnh Trên Lá Lúa (Rice Leaf Disease Detection)** là hệ thống tự động nhận diện và phân loại các loại bệnh thường gặp trên lá lúa thông qua hình ảnh. Hệ thống sử dụng mạng nơ-ron tích chập **CNN**, được xây dựng dựa trên **Keras** và **TensorFlow**, kết hợp với **OpenCV** để tiền xử lý ảnh.

Khi người dùng cung cấp một hình ảnh lá lúa bị bệnh, mô hình sẽ phân tích, trích xuất đặc trưng và dự đoán chính xác loại bệnh mà lá lúa đang mắc phải. 

## ✨ Tính năng nổi bật

- 🌾 **Nhận diện bệnh trên lá lúa:** Hỗ trợ nhận diện các loại bệnh phổ biến thông qua phân tích hình ảnh.
- 🚀 **Sử dụng CNN mạnh mẽ:** Tận dụng kiến trúc Convolutional Neural Networks với Keras và TensorFlow đem lại độ chính xác cao trong phân loại.
- 📊 **Tiền xử lý ảnh với OpenCV:** Tối ưu hóa chất lượng hình ảnh đầu vào để mô hình có thể trích xuất đặc trưng tốt nhất.
- 🌐 **Hỗ trợ chạy trên Google Colab:** Cung cấp sẵn notebook tương thích hoàn toàn với Google Colab (`Rice_Leaf_Detection_Colab.ipynb`) giúp dễ dàng huấn luyện mô hình với GPU miễn phí.

## 📂 Cấu trúc thư mục

```text
Rice-Leaf-disease-detection/
├── Rice_Leaf_Detection.ipynb        # Jupyter Notebook chính để huấn luyện và kiểm tra mô hình
├── Rice_Leaf_Detection_Colab.ipynb  # Phiên bản Notebook tương thích chạy trên Google Colab
├── classes.json                     # File JSON chứa thông tin ánh xạ nhãn (label mapping) của các bệnh
├── extract_code.py                  # Script trích xuất mã nguồn dự án
├── rice-leaf.zip                    # Tập dữ liệu (dataset) hình ảnh lá lúa
└── README.md                        # File tài liệu hướng dẫn
```

## 🚀 Hướng dẫn cài đặt & Chạy dự án

### 1. Chuẩn bị môi trường
Cài đặt các thư viện cần thiết (nếu chạy trên máy cá nhân):
```bash
pip install tensorflow keras opencv-python numpy matplotlib pandas
```

### 2. Giải nén dữ liệu
Giải nén tập dữ liệu hình ảnh trước khi huấn luyện:
- Cần giải nén file `rice-leaf.zip` ra thư mục tương ứng theo đường dẫn được cấu hình trong Notebook.

### 3. Chạy Notebook
- **Nếu chạy trên máy cá nhân:** Mở file `Rice_Leaf_Detection.ipynb` bằng Jupyter Notebook hoặc VS Code và chạy từng cell.
- **Nếu chạy trên Google Colab:** Tải file `Rice_Leaf_Detection_Colab.ipynb` lên Google Drive, mở bằng Google Colab, tải lên file `rice-leaf.zip` và chạy.

## 🧠 Nguyên lý hoạt động

1. **Nạp dữ liệu (Data Loading):** Đọc các hình ảnh từ tập dữ liệu được cung cấp.
2. **Chuẩn bị dữ liệu (Dataset Preparation):** Phân chia tập dữ liệu thành tập huấn luyện (train) và tập kiểm thử (validation/test).
3. **Ánh xạ nhãn (Label Mapping):** Sử dụng file `classes.json` để chuyển đổi nhãn bệnh từ dạng văn bản sang số để mô hình hiểu được.
4. **Tiền xử lý (Data Preprocessing):** Sử dụng OpenCV để thay đổi kích thước (resize), chuẩn hóa điểm ảnh (pixel normalization), và có thể augmentation hình ảnh.
5. **Xây dựng mô hình (Model Building):** Khởi tạo mạng CNN với các lớp Convolution, MaxPooling, Flatten và Dense bằng Keras.
6. **Huấn luyện (Training):** Huấn luyện mô hình phân loại dựa trên tập ảnh lá lúa và đánh giá độ chính xác.

## 👨‍💻 Sinh viên thực hiện
*Dự án thuộc Khoa Công nghệ thông tin - Chuyên ngành AI & IoT, Trường Đại học Đại Nam.*

- **Họ và tên:** Nguyễn Anh Dũng
- **Ngày sinh:** 26/06/2004
- **Lớp:** cntt-1605
