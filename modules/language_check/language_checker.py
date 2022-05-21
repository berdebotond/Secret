from msilib.schema import File


class LangaugeChecker:
    
    website_content: str
    file: File
    language_data = dict[str:str]
 
    def __init__(self, website_link: str) -> None:
        #db init
        self.website_content = self.__scrap(website_link)
        #
        self.__read_data()
        pass

    def __scrap(self) -> str:
        return ""

    #Read language_data.csv file to self.language_data
    def __read_data(self) -> str:
        return ""
    
    #Write self.language_data to language_data.csv
    def __write_data(self) -> str:
        return ""

    def teach(self) -> None:
        pass

    def language_check(self) -> str:
        pass

    def __del__(self) -> None:
        self.file.Close()
        self.__write_data()