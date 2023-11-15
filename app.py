import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Função para gerar a nuvem de palavras
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='viridis').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

# Configurar o tema e a cor de fundo
st.set_page_config(
    page_title="Nuvem de Palavras App",
    page_icon=":cloud:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Página principal do Streamlit
def main():
    st.title("Nuvem de Palavras App")
    st.markdown(
        """
        Aplicativo simples para gerar uma nuvem de palavras.
        Pressione o botão abaixo para iniciar o processo.
        """
    )

    # Adicionar um botão para iniciar o processo
    if st.button("Gerar Nuvem de Palavras"):
        text = (
            'apple inc wikipedia jump content main menu main menu move sidebar hide navigation main pagecontentscurrent eventsrandom articleabout wikipediacontact usdonate contribute helplearn editcommunity portalrecent changesupload file language language link top page across title search search create accountlog personal tool create account log page logged editor learn contributionstalk content move sidebar hide top 1history toggle history subsection 1119761980 founding incorporation 1219801990 success macintosh 1319901997 decline restructuring 1419972007 return profitability 1520072011 success mobile device 162011present postjobs era tim cook 2products toggle product subsection 21mac 22iphone 23ipad 24other product 25services 3marketing toggle marketing subsection 31branding 32advertising 33stores 34market power 35customer privacy 4corporate affair toggle corporate affair subsection 41business trend 42leadership 421senior management 422board director 423previous ceo 43corporate culture 44offices 45litigation 5finances toggle finance subsection 51taxes 52charity 6environment toggle environment subsection 61apple energy 62energy resource 63toxins 64green bond 7supply chain toggle supply chain subsection 71worker organization 8see also 9references toggle reference subsection 91bibliography 10further reading 11external link toggle table content apple inc 146 language afrikaansalemannischanaraskielangliscaragonesasturianuazrbaycancabanlamgu bosanskibrezhonegcatalacestinacymraegdanskdavvisamegielladeutschdine bizaadeestiespanolesperantoeuskarafroysktfrancaisgaeilgegalegohakkangihausahrvatskiigbobahasa indonesiainterlinguaisixhosaisizuluislenskaitalianojawakiswahilikreyol ayisyenkurdilatinalatviesuletzebuergeschlietuviula lojbanlombardmagyarmalagasybahasa melayuminangkabau mingdengngunahuatlnederlands norsk bokmalnorsk nynorskoccitanozbekcha palzischpapiamentuplattduutschpolskiportuguesqaraqalpaqsharomanarumantschruna simi sardushqipsicilianusimple englishslovencinaslovenscinaslunskisoomaaliga srpskisrpskohrvatski sundasuomisvenskatagalog tatarcaturkceturkmence uyghurchevenetotieng vietwinarayyorubazazakizeeuws'
        )
        generate_wordcloud(text)

# Executar o aplicativo
if __name__ == "__main__":
    main()
