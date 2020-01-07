mysqldump -uroot -ppassword stocktrading user_table > user_table.sql
mysqldump -uroot -ppassword stocktrading django_admin_log > django_admin_log.sql
mysqldump -uroot -ppassword stocktrading news > news.sql
mysqldump -uroot -ppassword stocktrading stock_comment > stock_comment.sql
mysqldump -uroot -ppassword stocktrading comment_reply > comment_reply.sql

mysqldump -uroot -ppassword stocktrading > stocktrading.sql