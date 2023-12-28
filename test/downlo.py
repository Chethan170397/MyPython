def download_tar_archive(self):
        destination_path = self.compressed_path
        filename = f"{self.unique_name}.{self.source_type.lower()}"

        self.compressed_file_path = os.path.join(destination_path, filename)

        if os.path.exists(self.compressed_file_path):
            self.logger.info('file already downloaded skipping download')
            return

        response = requests.get(self.source)

        if response.status_code == 200:
            with open(self.compressed_file_path, 'wb') as file:
                file.write(response.content)
            self.logger.info("tar file downloaded successfully.")
            return True
        else:
            self.logger.info("Failed to download the tar file.")
            return False

    def download_zip_archive(self):
        destination_path = self.compressed_path
        filename = f"{self.unique_name}.zip"

        self.compressed_file_path = os.path.join(destination_path, filename)

        if os.path.exists(self.compressed_file_path):
            self.logger.info('file already downloaded skipping download')
            return

        response = requests.get(self.source)

        # if 'Content-Disposition' in response.headers:
        #     # Get the filename from the content disposition
        #     content_disposition = response.headers['Content-Disposition']
        #     filename = urllib.parse.unquote(content_disposition.split('filename=')[1])
        # else:
        #     # Get the filename from the URL
        #     parsed_url = urllib.parse.urlparse(self.source)
        #     filename = urllib.parse.unquote(parsed_url.path.split('/')[-1])

        if response.status_code == 200:
            with open(self.compressed_file_path, 'wb') as file:
                file.write(response.content)
            self.logger.info("Zip file downloaded successfully.")
            return True
        else:
            self.logger.info("Failed to download the zip file.")
            return False


