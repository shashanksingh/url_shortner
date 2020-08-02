CREATE TABLE Urls (
    `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
    `long_url` varchar(2048) NOT NULL,
    `short_url` varchar(255) NOT NULL,
    `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
    `long_url_hash` varchar(512) NOT NULL, /* To enforce one long url is one short url*/
    PRIMARY KEY (`id`),
	UNIQUE INDEX long_url_hash_uniqueness_constraint (long_url_hash) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
