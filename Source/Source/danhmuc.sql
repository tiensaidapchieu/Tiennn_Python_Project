-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 03:00 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `ten_danh_muc` varchar(100) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1,
  `ngay_tao` datetime DEFAULT current_timestamp(),
  `ngay_cap_nhat` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danh_muc`, `mo_ta`, `trang_thai`, `ngay_tao`, `ngay_cap_nhat`) VALUES
(1, 'Hot Sale', 'Sản phẩm đang khuyến mãi', 1, '2025-11-04 07:39:01', '2025-11-04 07:39:01'),
(2, 'Thuốc', 'Các loại thuốc kê đơn và không kê đơn', 1, '2025-11-04 07:39:01', '2025-11-04 07:39:01'),
(3, 'Thực phẩm chức năng', 'Bổ sung dinh dưỡng và vitamin', 1, '2025-11-04 07:39:01', '2025-11-04 07:39:01'),
(4, 'Thiết bị, dụng cụ y tế', 'Dụng cụ y tế, máy đo, bông băng', 1, '2025-11-04 07:39:01', '2025-11-04 07:39:01'),
(5, 'Mỹ phẩm AN NAM', 'dễ sử dụng', 1, '2025-11-04 07:39:01', '2025-11-04 08:27:59'),
(6, 'Chăm sóc cá nhân', 'Sản phẩm vệ sinh và chăm sóc cơ thể', 1, '2025-11-04 07:39:01', '2025-11-04 07:39:01'),
(11, 'Phạm Minh Tiến', '077205004275', 1, '2025-11-04 08:57:10', '2025-11-04 08:57:10'),
(12, 'Văn Minh Nhật', '075205014392', 1, '2025-11-04 08:57:35', '2025-11-04 08:57:35');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
