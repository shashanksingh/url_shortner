CREATE TABLE `Urls` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `long_url` varchar(2048) NOT NULL,
  `short_url` varchar(255) NOT NULL,
  KEY `id` (`id`),
  KEY `long_url` (`long_url`(1024))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;