from pyradios import RadioBrowser
from models import Radio

class RadioBackend:
    def __init__(self):
        self.rb = RadioBrowser()

    # قائمة بأسماء المحطات
    names: list[str] = [
      'إذاعة القرآن الكريم (القاهرة)', # Egypt
        'Saudi Quran',  # Saudi Arabia
        'Quran Radio راديو القرآن - Kuwait الكويت',  # Kuwait
        'Dubai Holy Quran',  # Dubai
    ]

    def get_radios(self):
        results: list[Radio] = []
        # البحث عن كل محطة في القائمة
        for name in self.names:
            radios = self.rb.search(name=name, name_exact=False)
            for radio in radios:
                print(f"Original URL: {radio['url']}")  # Debug: Original URL from pyradios
                resolved_url = radio['url']
                results.append(
                    Radio(
                        country_code=radio['countrycode'], 
                        title=radio['name'], 
                        audio_url=resolved_url
                    )
                )
        
        return results
