from pyradios import RadioBrowser
from models import Radio

class RadioBackend:
    def __init__(self):
        self.rb = RadioBrowser()
    
    # قائمة بأسماء المحطات
    names: list[str] = [
        "إذاعة القرآن الكريم من القاهرة",#egypt
        'Saudi Quran', #saudi arabia
        '#إذاعة القرآن الكريم',#jordan
        'Quran Radio راديو القرآن - Kuwait الكويت',#kuwait
        'Dubai Holy Quran', #dubai
        # 'Quran Radio Station-Nablus',
        # 'Radio Quran Karim',
        # 'قرآن، طعم آفتاب (زنده)'
        # 'إذاعة طريق السلف'#libya
    ]

    def get_radios(self):
        results: list[Radio] = []

        # البحث عن كل محطة في القائمة
        for name in self.names:
            radios = self.rb.search(name=name, name_exact=False)
            for radio in radios:
                results.append(
                    Radio(
                        country_code=radio['countrycode'], 
                        title=radio['name'], 
                        audio_url=radio['url_resolved']
                    )
                )
        
        return results