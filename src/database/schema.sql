CREATE TABLE Urls (
    `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
    `long_url` varchar(2048) NOT NULL,
    `short_url` varchar(255) NOT NULL,
    `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
	UNIQUE INDEX short_url (short_url)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
