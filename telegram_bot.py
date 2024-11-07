import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#posledni citat 29.3.2023
# Tvůj token z BotFather
TOKEN = '7721163593:AAHWXucyvElDWSqtjcirTzWwbrNNYb2cKec'

# Seznam citátů
citaty = [
    "Jak by byl krásný svět, kdyby každý občan, chválící nějaký stát, musel tam i žít.",
    "Nestěžujte si pořád na drahotu. Vždyť máte všechno o hodně levnější než příští rok.",
    "Představ si, že by ti někdo nabídl sto tisíc Euro, za podmínky, že tisíc si můžeš nechat a zbytek musíš předat svému největšímu nepříteli. Vzal bys ty prachy?",
    "Kam nedojdeš pěšky, tam být nemusíš.",
    "Někdy je příjemné cítit strach. Zvlášť, když není váš."
    "Jak by byl krásný svět, kdyby každý občan, chválící nějaký stát, musel tam i žít.",
    "Pravý hrdina z boje nikdy neustoupí, i kdyby ho to mělo stát život! Pravý bojovník z boje uteče... A vrátí se s větším klackem!",
    "Sebehorší situace nakonec dopadne dobře. Jen již nemusíš být součástí toto konce.",
    "Moudrost se buduje ve chvílích, kdy posloucháš i když bys radši mluvil.",
    "Neříkám lidem, zda jsem vlastenec. Až bude jednou zle, třeba to o mě řekne vlast."
    "Největší slaboši opouštějí svět vlastní rukou. A pak také ti nejsilnější.",
    "S trpělivostí dostaneš vše, co zasloužíš. Ne, co chceš! Jen co zasloužíš..",
    "Lidé rádi mluví o pravdě. Přesto jim lži nevadí, pokud lžete v jejich prospěch.",
	"Osamělost moudrých často vzniká z touhy sdělit myšlenky, které považují za důležité, avšak druzí je vnímají jako nepřípustné.",
	"Lidskou zlobu si neberu osobně. Jsem svědek, ne cíl.",
	"Devadesát procent kritiky je manipulace. Tak nekritizuj a řekni jasně, co chceš.",
	"Až jednou najdu odvahu, navštívím každou ženu, se kterou jsem kdy měl vztah a upřímně se jí omluvím. Dochází mi bohužel, že vždycky je za co.",
	"Nechozené stezky zarůstají. V lesích i v srdcích.",
	"Někdy ti dá Bůh dar jen aby se pobavil.",
	"Lidé touží po pravdě, přičemž nejvíc šíří pomluvy a lži. Co jsme, to dostáváme.",
	"Kvalita často vítězí nad kvantitou. Nejúčinnější je však hodně kvality.",
	"Důvěra je levnou náhražkou kontroly. My s dýkou a pláštěm nespoléháme na náhražky.",
	"Nezkoumej moji mysl, pokud jsi ještě nepoznal tu svou.",
	"Zkus být správnou kapkou v moři a i moře bude v pohodě..",
	"Dívčí pláč a psí kulhání nemívá dlouhého trvání.",
	"Šetři důvěrou k lidem, kteří se o tebe zajímají. Těch, co chtějí poznat tvé nitro, potkáš jen pár za život. Většina sleduje vlastní zájmy, nebo zkoumá tvá slabá místa.",
	"Meditace z tebe tesá lepšího člověka. Lepšího, než jsi byl. Ne, než jsou druzí.",
	"Meče se kovají, nože se kalí. Muži se chystají, zbabělci balí.",
	"Klidně věř, že víš, co je po smrti. To, co přijde, tě stejně dostane.",
	"To, co bylo zjeveno, nemá být dál sděleno. Což je velké břemeno..",
	"Pokud někoho opravdu miluješ, dej mu volnost! Pokud se vrátí, je tvůj, když ne, stejně ti nikdy nepatřil... Až tehdy je třeba vystopovat ho a zabít...",
	"Češi jsou úžasný národ. Škoda, že nebyli už u stvoření světa. Mohli hodně poradit.",
	"Psychicky zdravý člověk nemůže být zlý. Může být jen zlem postižený.",
	"Která víra vyžaduje největší odvahu? Víra v lidi..",
	"Nejlepší chvíle ke změně tvého života byla před dvaceti lety. Druhá nejlepší je dnes.",
	"Vesmír ti vydá vše, o co vytrvale žádáš. Žádej však řečí činů. Mluvení je jen šum.",
	"Ještě to víčko teď z každé PET flašky před pitím ukroutit. Jakoby ten život už tak nebyl těžkej..",
	"Číháš v tichu na zlé lidi, pracuješ pro hloupé lidi. Úspěchy tvé tajné práce nikdo nikdy neuvidí.",
	"Může zmizet člověk? Ani v demokracii neexistuje lidský život, který by měl větší cenu než národní bezpečnost.",
	"Snídej sám, o oběd požádej přítele a k večeři sněz nepřítele..",
	"Miminko přichází na svět s dvěma vrozenými vlastnostmi: Ničeho se nebojí a nestará se, co si o něm kdo myslí. Taky jsi ty vlastnosti měl.",
	"Žena je jako výstroj pro krizové situace. Každá kvalitní je už sbalená..",
	"Dovol člověku porušit pravidla a pochopí to jako své právo.",
	"Jsi-li pokorný, budeš pro mnohé přítel. Jsi-li agresivní, budeš pro mnohé hrdina. Jsi-li spravedlivý, budeš pro mnohé legenda.",
	"Netrestejte doma partnera za depky, které jste si dotáhli z venku.",
	"Radši padnout do oka holce od vedle, než odstřelovači od naproti.",
	"Skutečně zamilované ženy se nikdy nevzdávají. Nikdy se nevzdávají ani muži, kteří nemají co ztratit. Příroda každému nadělila jiný druh síly, která je jejich mocí i jejich prokletím.",
	"V těžkých obdobích lidé nejdříve rezignují na hygienu, pak na soucit k druhým a nakonec na žití v pravdě..",
	"Nehraj si se srdcem ženy! Má jen jedno. Hraj si s ňadry. Ty má dvě..",
	"Lidé mluví sprostě, aby předvedli, že jsou svobodní. Přitom jsou jen sprostí..",
	"Najdi vlky. Žij s vlky. Pochop vlky. Ovládni vlky.",
	"Nikdy neruš svého nepřítele, když dělá nějakou chybu.",
	"Mohou-li být Tvá slova zle pochopena, budou zle pochopena..",
	"Žena je jako jeskyně s pokladem. Trvá dlouho, než tě pustí dovnitř. Pak ale udělá vše, abys už nikdy neodešel.",
	"Když už musíš před lidmi hrát nějakou roli, hraj sebe.",
	"To, co hledáš si už neseš pevně v sobě. Stejně tak to, před čím utíkáš.",
	"Pokud tě něco donutilo nenávidět, tak jsi prohrál.",
	"Skuteční přátelé Ti přejí, ať se máš dobře. Ale ne líp než oni..",
	"Tři věci v životě nejdou nikdy vrátit: čas, slovo a šance.",
	"Žádáš-li lidi o rady, odpoví ti jeden anděl a deset démonů..",
	"Nejupřímnější mužský kompliment k ženě je erekce a k muži závist..",
	"Nejlepším způsobem jak předvídat vlastní budoucnost je tvořit si ji.",
	"Netoužím po pravdě.  Toužím po příbězích. Učím se od lidí. Nevychovávám je.",
	"Na co je tvor, co netvoří...",
	"Buď schopen být krutý. A pak nebuď krutý. Protože slušný neznamená slabý.",
	"Když se zkoušíš ptát Boha, neposlouchej figurky, které chtějí odpovídat za něj.",
	"Máš v životě vždy volbu? Ano! Ale někdy jen z možností, které se ti nebudou líbit...",
	"Častá samota většině lidem ublíží. Pro umělce, Ninji a mystiky je to však prostředek k dosažení cíle.",
	"Každý psychopat je jiný. A to je dobře. Kdyby byli všichni stejní, bylo by to normální..",
	"Mnozí chlapi, toužící po respektu, dělají vše pro to, aby ho neměli..",
	"Sprosťáka polituj, hlupáka pouč. A když se nezmění, s úctou se rozluč.",
	"Když dojdeš na vrchol, nebude tam nikdo, kdo by tě pochválil, nebo ti pomohl.",
	"Neposlouchej názory lidí, za kterými bys nešel pro radu.",
	"Pracuj jako Mystik, uvažuj jako Filozof a hovoř jako prosťáček. Aby ti lidé věřili, nesmíš ohrozit jejich ego..",
	"Ženy jsou jako malé rostlinky. Pokud ti má vykvést jedna, měl bys vytrhat ty kolem.",
	"Někdy musíš sedmkrát zalhat, abys směl říct v jedné větě pravdu.",
	"Smrt je jediná činnost, kterou zvládne opravdu každý.",
	"Slabí lidé potřebují k někomu vzhlížet a někoho nenávidět.",
	"Pokora v obdivu je póza. Pokora v příkoří je čest.",
	"Hněv posiluje! A oslepuje.",
	"Smysl žití dává jeho cíl. Může být i malý, ale měj ho.",
	"Když smečka roste, objeví se zrádci.",
	"Čím vyšší poznání, tím méně přátel.",
	"Sytý hladovému nevěří. Hladový sytého nechápe.",
	"Pokud na oblíbeném člověku nevidíš nic, co by ti vadilo, pak jej ještě neznáš dost.",
	"Čím víc víš, tím hůř spíš..",
	"Moudrost se buduje ve chvílích, kdy posloucháš i když bys radši mluvil.",
	"Ať už se ti v minulosti stalo cokoliv, svět ti není nic dlužen.",
	"Němci dnes obchodují a Židé bojují. Divný svět..",
	"Dej si pozor na pastýře, kterého chválí vlci.",
	"Lidé většinou chápou, co mají v životě dělat. Ale nedělají to.",
	"Když čelíš výzvám sám, nemáš se o koho strachovat. A taky na koho žalovat..",
	"Čím slabší národ, tím větší lakota, nesnášenlivost a zbabělost.",
	"Slovo muže platí! Proto s ním neplýtvej.",	
	"Víra je vše u čeho jsi nebyl osobně.",
	"Proč v lidech propukne nenávist k jinému národu jen proto, že se rozhodl bránit? Možná jim ten hrdinský boj připomíná, že by toho sami nebyli schopni.",
	"Žijeme ve světě, kde každý prosťáček ví, co je špatně. Hlavně na těch druhých..",
	"Neomlouvej žádnou válku. Zabraň válce, která probíhá.",
	"Kdo je vlastně kamarád? Ten, co ti při návštěvě nutí panáka, nebo ten, co pro tebe koupí bylinkový čaj? Kamarád tě dobře zná, přítel tě i respektuje ...a malé věci v chování o nás nejvíce řeknou.",
	"Neobdivujte lidi jenom za tvrzení, že rozjeli byznys v garáži. Zvlášť, pokud jediný jejich problém byl, kam postavit fotrův mercedes..",	
	"Manipulátoři mívají psí oči.",
	"Něco vyššího mě nutí, bývat k lidem pravdivý. Abych tedy neškodil, bývám často sám.",
	"Neatakuj, nebraň se, neargumentuj! Prostě vyslov názor a potom pevně stůj..",
	"V životě můžeš získat v podstatě cokoliv. Avšak jen, pokud se všeho ostatního vzdáš.",	
	"Pro politické cíle lze zpochybnit všechno. I zjevné utrpení.",
	"Když si lidé zvyknou na blahobyt, měl by přijít pád.",
	"Než začnete příteli vnucovat vlastní názory, upřímně se zajímejte, proč má ty jeho.",
	"Poznej, používej, ale nevnucuj. Včela nevysvětluje mouše, že med je lepší než hovno.",
	"Za každým úspěšným mužem najdeš opuštěnou ženu..",
	"Bolest je další zpráva těla, když jsi tu předchozí neslyšel.",
	"Nikdo tady není pro to, aby plnil tvoje sny. Každý si má plnit ty své.",	
	"Nadávky jsou slzy slabých mužů.",
	"Nejhorší nemoci nevzniknou tím, co jíš, ale tím, co žere tebe!",
	"Nežádej věrnost. Dočkáš se zrady. Nedoufej v pomoc. Přijdou jen rady.",
	"Chceš-li mír, chystej válku. Chceš-li válku, začni válku.",
	"Obávej se starého vojáka v jednotce, kde jiní umírají mladí.",
	"Nula od nuly pojde. Debilům hodně projde..",
	"Osud slabé lidi láme, ale silným uhne.",
	"Muž stárne jako víno. Žena stárne jako mléko.",
	"Nedůležité, kdo zplodil. Důležité, kdo vychová.",
	"Důvod, proč vyhynuli draci, je, že došly princezny.",
	"Sedneme na lep každému, kdo nám nakuká, že jsme pašáci.",
	"Dělej co máš rád a problémy přijdou samy..",
	"Pokud muž nejedná, měl by sbírat informace. Pokud nedělá ani to, měl by spát.",
	"Prázdná kapsa není překážkou úspěchu. Prázdná hlava a prázdné srdce naopak ano.",
	"Vše nakonec dobře dopadne. Pokud něco dobře nedopadlo, tak to ještě neskončilo.",
	"Tajemství vydané všem, není sdílené, ale zničené.",


	
	
	
	
	
	
	
]

# Funkce pro příkaz /citát
async def citat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    citat = random.choice(citaty)
    await update.message.reply_text(citat)


# Hlavní funkce
def main():
    # Inicializace bota s tokenem
    app = ApplicationBuilder().token(TOKEN).build()

    # Přidání handleru pro příkaz /citát
    app.add_handler(CommandHandler("citat", citat))

    # Spuštění bota pomocí polling, aby běžel nepřetržitě
    app.run_polling()

# Spuštění hlavní funkce
if __name__ == '__main__':
    main()
