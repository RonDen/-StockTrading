/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : stocktrading

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 07/01/2020 19:35:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for optional_stock_table
-- ----------------------------
DROP TABLE IF EXISTS `optional_stock_table`;
CREATE TABLE `optional_stock_table`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_of_shares` int(11) NULL DEFAULT NULL,
  `stock_id_id` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `optional_stock_table_user_id_id_stock_id_id_06b2c297_uniq`(`user_id_id`, `stock_id_id`) USING BTREE,
  INDEX `optional_stock_table_stock_id_id_cf330a51_fk_stock_info_stock_id`(`stock_id_id`) USING BTREE,
  CONSTRAINT `optional_stock_table_stock_id_id_cf330a51_fk_stock_info_stock_id` FOREIGN KEY (`stock_id_id`) REFERENCES `stock_info` (`stock_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `optional_stock_table_user_id_id_6812784d_fk_user_tabl` FOREIGN KEY (`user_id_id`) REFERENCES `user_table` (`phone_number`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of optional_stock_table
-- ----------------------------
INSERT INTO `optional_stock_table` VALUES (5, 40, '000002', '19959008351');
INSERT INTO `optional_stock_table` VALUES (6, 3, '000010', '19959008351');

SET FOREIGN_KEY_CHECKS = 1;
