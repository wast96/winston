#!/usr/bin/env python3
"""Generate out/ch24_bilingual.md with GUARANTEED verbatim source quotation.

Reads the source paragraphs from data/src/52_text00049.txt, pairs each (in
reading order) with a hand-authored English paragraph, and emits the '>'/English
bilingual QC file. The source is never re-typed here: it is read from disk and
quoted byte-for-byte, and the script asserts that the concatenation of every
blockquote equals the source content character-for-character before writing.

Source structure (ch24, 第二十四章 巳初 -- the FINAL chapter):
  raw[0]  L1        : 巳初        -> absorbed into the H2 chapter title (not a para)
  raw[1..3] L2+L3+L4: opening vignette, extractor-split (L2/L3 end on commas) ->
                      MERGED into one paragraph; recurs VERBATIM at raw[223] (L223)
  raw[4..5] L5+L6   : dateline (巳初), extractor-split -> MERGED (L6 is a single "。")
  raw[6..354] L7..L355 : body (349 paragraphs); L355 is （全文终）"The End"
  raw[355] L356     : the source's per-chapter time-gloss -> the source's own italic note
                      HOUR MATCHES: gloss describes 巳/9 a.m. (Snake), = nominal hour 巳初.
  raw[356] L357     : U+200B zero-width space -> dropped
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "src", "52_text00049.txt")
OUT = os.path.join(ROOT, "out", "ch24_bilingual.md")

TITLE_EN = "Chapter Twenty-Four. The Hour of the Snake, First Half (9 a.m.)"

# The opening vignette (L2+L3+L4, merged) recurs VERBATIM at L223; one constant.
VIG = ("If some immortal were to look down upon the whole of Chang'an, he would "
       "see, upon the empty streets, two little black specks racing desperately "
       "along, one going south, one going east, drawing nearer and nearer, until "
       "at last they met and came together at the crossroads of Yongchong and "
       "Xuanping.")

# --- English paragraphs, in source reading order --------------------------------
BODY = [
# vignette (raw1+2+3, merged; recurs at raw223)
VIG,
# dateline (raw4+5, merged)
"The third year of Tianbao, the fifteenth day of the first month; the hour of the Snake, first half.",
# L7 (raw6) location line
"Chang'an; Wannian County; the Yanxing Gate.",
# L8
"There came a heavy tramp of footsteps as a great body of guard-soldiers hurried up onto the top of the wall and set off at a run toward the north. The right flank of this long file happened to fall full in the light of the morning sun rising in the east, and their armor threw off a stabbing glare. Seen from afar, it was as though a bright border had been inlaid along the upper edge of the city wall.",
# L9
"At their head was the gate-commander of the Yanxing Gate. He ran in an unseemly scramble, without even time to knot the silk cords of his armor, so that the heart-guarding mirror-plate hung askew upon his chest, looking rather comical. But he would not stop so much as to set his appearance to rights; he only pelted on, his face at once bewildered and tense.",
# L10
"Only just now they had received a strange letter. It had been brought by a Hu named Aluoyue, and on it was written but a single line: 'The Son of Heaven is at the lowering-frame north of the Yanxing Gate.' It was signed by a Commander of the Jing'an Bureau. The gate-commander found it all rather baffling. The Son of Heaven? Was the Son of Heaven not up on the Qinzheng Wuben Tower? How should he have got out there? And who was this Commander of the Jing'an Bureau?",
# L11
"Yet baffling did not mean to be ignored. The word 'Son of Heaven' stood in the message, and come what might the gate-commander must go and see. And most of all at such an extraordinary time as this: there could be not the least oversight.",
# L12
"He hurriedly mustered a dozen-odd guard-soldiers, saw them fully armed and armored, and led them out to look in person. The party ran a stretch along the wall-top, and from afar they could already see that huge lowering-frame. The gate-commander put a hand to his brow to shade off the stabbing light, and made out dimly what seemed to be a man sprawled beside the frame, motionless.",
# L13
"The man wore a robe of scarlet-yellow, his hair in disarray, and near him on the ground there had rolled a tongtian crown... At the sight of this the gate-commander's heart gave a lurch: it seemed the letter had told no lie. His steps quickened, criss-crossing faster, and soon he had rushed up beside the frame; but when he was still a few paces from the man he stopped short all at once, and looked warily on.",
# L14
"Though the gate-commander had never once beheld the Son of Heaven's face, yet the coiling dragons embroidered on that robe, the golden Boshan at the front of the tongtian crown, the liuhe boots upon the feet, every one of them proved the man before him to be of the most exalted station. He dared hesitate no further; hastily he bent down and, with all reverence, turned that person over.",
# L15
"The Son of Heaven was still sunk in a swoon, but breathing yet. The gate-commander made a quick examination and found that, save for a bruise upon the forehead, he had no grave hurt; and only then was his heart set at ease.",
# L16
"Just then a shout went up from the soldiers beside him. The gate-commander turned his head and found that, hung on the outer side of the lowering-frame, there dangled a great rattan pannier tilted all askew, and within it lay, likewise senseless, a beautiful female Daoist. Stranger still, beside the pannier, at the lower end of the hoisting-rope, there hung the corpse of a man, swinging to and fro against the wall.",
# L17
"The gate-commander thrust his head out over the wall and saw that a great hole had opened in the ice of the moat below, which showed that someone had once leapt down from this very spot.",
# L18
"Such a strange arrangement he could by no means puzzle out, think as he might.",
# L19
"But this was not the most pressing thing. What most needed doing was to get the Son of Heaven back to the palace with all speed, for over there, no doubt, things were already in an uproar. Thinking so, the gate-commander could not help looking off to the north. Now that day had broken, the view within the city had grown very clear. The Taishang Xuanyuan Lantern-Tower had vanished away, and a thick black smoke went streaming and blowing over toward the Xingqing Palace, fouling one corner of the deep-blue sky.",
# L20
"The gate-commander straightened up, took the flag and the golden gong from a subordinate's hands, first struck the great gong, and then swiftly signaled with the flag toward the nearest watchtower. The signal was soon caught by that watchtower and passed on in all directions with speed. In a moment the flags of the watchtowers all over the city were flying, and the beat of gongs rose on every side. Anyone who could read them would have found that all bore the selfsame message:",
# L21
"'The Son of Heaven is unharmed!'",
# L22
"Chen Xuanli glared with venomous hatred at the one-eyed man being held up before him, and could have wished to spring forward and cut him down at a stroke. It was this man who, before all the assembled officials, had struck him senseless; it was this man who had openly carried off the Son of Heaven; it was this man who had thrown the whole of Chang'an into vast upheaval.",
# L23
"For a guards-commander of the Longwu Army there could be no greater humiliation than this.",
# L24
"Now he had only to crook his finger down half a hair, and this fellow guilty of so monstrous a crime would be turned into an iron hedgehog. Yet Chen Xuanli of all things dared not stir: the Son of Heaven was to this hour nowhere to be found, and everything must still be brought home through Zhang Xiaojing. This scoundrel could not yet be let to die.",
# L25
"At the thought Chen Xuanli glanced a little aside. Prince Yong stood at his very shoulder, his robe all filthy with soot. This scion of the imperial house had his eyes fixed hard on what lay ahead, and they too were filled with the flames of wrath.",
# L26
"Chen Xuanli recalled it now: last year, so it was said, there had been a great case, and it had had something to do with this very Zhang Xiaojing and Prince Yong; the prince had come off much the worse, and Zhang Xiaojing had been flung into the death cells. Small wonder that, up in the Star-Plucking Hall just now, Zhang Xiaojing had singled Prince Yong out to kill.",
# L27
"But the prince's luck was uncommonly good: he had, of all things, come out alive from under Zhang Xiaojing's murderous hand. Chen Xuanli was not without his doubts as to how the prince had escaped; yet since he was still alive, there was no need to breed fresh trouble over it. The safety of the Son of Heaven was, just now, the most important thing of all.",
# L28
"'Zhang Xiaojing, you are surrounded already. Speak, and be quick: where have your confederates carried the Son of Heaven off to?!' Chen Xuanli bellowed in a voice of full-throated force.",
# L29
"Wen Ran and Cen Shen, hearing it, changed color at the same instant. Never had they dreamed that Zhang Xiaojing had, of all things, carried off the Son of Heaven! Here was a case that towered to the very heavens. But shock was shock: Wen Ran's grip on Zhang Xiaojing's arm only tightened the more. She said low to Cen Shen: 'Young master Cen, go, quickly. We cannot drag you down with us any longer.' This time Cen Shen made no more grand speeches; he only gave a heavy grunt of assent.",
# L30
"To carry off the Son of Heaven was a crime to be visited on the whole nine degrees of kin; the calamity would not stop at one man alone. However little Cen Shen himself feared death, he had his family to think of.",
# L31
"But before he could make any move, Feng Dalun had thrust himself to the fore, and, pointing with venom at the two of them, cried out in a loud voice: 'These two are Zhang Xiaojing's accomplices! Everything that has happened is of their doing!'",
# L32
"Feng Dalun did not in the least know what had befallen at the Xingqing Palace, but he knew that the matter touched the Son of Heaven, and so must be a case that shook heaven and earth; he must seize this chance to bite these fellows to death, and hard. Whatever filth there was to fling, he would fling it all their way.",
# L33
"This accusation of Feng Dalun's set the ranks astir. Chen Xuanli raised a hand and rebuked it sharply, then turned his head and bellowed once more: 'Zhang Xiaojing, tell me quickly where the Son of Heaven is, and you may yet keep a whole corpse!' Prince Yong stood to one side, both hands hanging within his sleeves, eyes narrowed, and said not a word.",
# L34
"Wen Ran bit her lip, resolved to walk this last stretch of the road beside her benefactor. All at once she felt the crook of her arm stir: Zhang Xiaojing had lifted his neck, and in a hoarse rasp said, 'First let those two go, and then I will tell you.'",
# L35
"Chen Xuanli flew into a rage: 'You cur of a slave, would you still haggle terms?!'",
# L36
"'Yes.'",
# L37
"Zhang Xiaojing knew that this time there was no escape at all: even were he now to declare who he was and explain, it would avail nothing. Chen Xuanli, Prince Yong, Feng Dalun, none of them would ever believe him, none of them would ever let him go. But Wen Ran and Cen Shen were innocent.",
# L38
"Chen Xuanli gripped his sword-hilt, his fury bursting up. Feng Dalun, in dread that he might yield, hastened to warn him: 'General Chen, this death-row convict has committed a string of bloody crimes before this, and is cunning and cruel past belief; give him but a thread of a chance, and it may brew a great disaster.' He turned again and said with all deference to Prince Yong: 'To this, Your Highness can bear witness.'",
# L39
"Prince Yong gave a cold snort, neither gainsaying nor seconding it. Feng Dalun thought it strange: Prince Yong hated Zhang Xiaojing to the marrow; why did he not seize this perfect chance to fling a stone down the well? Then a second thought made all clear to him: Zhang Xiaojing was doomed in this pass whatever came, and Prince Yong, standing on his dignity, need not raise a hand himself. But that the prince was unwilling to act did not mean he was unwilling to see others act; and this was the very best moment to do a man a favor.",
# L40
"His mind made up, Feng Dalun took a step forward: 'Zhang Xiaojing, you have now committed a crime past all pardon, and are hemmed in by a great host; do you still cling to such fond and foolish hopes? I tell you: if you do not say where the Son of Heaven is, you will die most horribly today! And not you alone, those about you will fare worse yet! That little whore called Wen Ran, every man of our Bear Fire Gang will have his turn at her, three days and three nights at the least, and not one hole in her body will be let to rest!'",
# L41
"As he went on Feng Dalun waxed ever more pleased with himself, and ever fouler of tongue. He did not care a whit where the Son of Heaven was; he wanted only to goad Zhang Xiaojing past all bearing, so that the Longwu Army should have its pretext to strike. Until he saw the corpse of the Five-Faced Yama, Feng Dalun's heart could find no true peace.",
# L42
"Chen Xuanli, hearing Feng Dalun grow coarser and coarser, could not but knit his brows; yet he did not speak to stop him. He too wished to know whether such talk could indeed force out Zhang Xiaojing's last defenses.",
# L43
"Feng Dalun spattered spittle as he spoke, in the full flush of his glee. Then Zhang Xiaojing all at once wrenched free of Wen Ran's and Cen Shen's support, drew his whole body up and stood erect with three steps forward, and the single eye kindled once more with a keen killing-light. Feng Dalun, caught off his guard, started back in fright and sat down hard on the ground, and that fear rooted in the very marrow of his bones spread anew through all his limbs and frame.",
# L44
"Zhang Xiaojing swayed as if about to fall; that lunge just now had been but a last mustering of his breath. Wen Ran rushed up to hold him, but he pushed her gently aside and spoke toward those across from him:",
# L45
"'General Chen, at this same hour yesterday, Deputy Director Li fished me out of the death cells and required of me that I settle the matter of the Türk Wolf Guards. Can you guess what reason he used to win me over?' Zhang Xiaojing's voice had but newly come back to him, hoarse past all telling, like the hot desert wind of the Western Regions blowing over rolling sand.",
# L46
"Chen Xuanli was taken aback, not knowing why he should suddenly bring up so irrelevant a matter. Zhang Xiaojing did not look for him to answer; he only gave a self-mocking smile and went on:",
# L47
"'First he set forth the great bond of prince and subject, said he would pardon my capital crime and grant me the substantive post of deputy general of a senior garrison; then he asked whether I hated the Türks, and offered me a chance for revenge. But none of these things moved me. What truly made me resolve to help him was one sentence he spoke: This affair today has nothing to do with the Son of Heaven's face, nor with the career of me, Li Bi; it is for the safety of a whole city of common folk! Here are the lives of hundreds of thousands.'",
# L48
"Before the Yixiang Pavilion all was still; commander and Longwu soldier alike seemed drawn in by Zhang Xiaojing's words. Every one of them had family living within the city; every one of them was closely bound up with this matter.",
# L49
"'I served ten years as a soldier of the Western Regions and nine years as a buliang chief, all for the sake of two words: peace and safety. I stand alone in the world; I ask only that this city I have shared my mornings and evenings with should be safe, that every man and woman within it may go on living their happy and ordinary lives. So I promised Deputy Director Li that I would do all in my power to stop this one attack, though it should cost me my own life, and I would not grudge it.'",
# L50
"As he said this Zhang Xiaojing put out his right fist and struck it lightly against his left shoulder. Others did not know the sense of the gesture, but Chen Xuanli understood it. He had risen from the ranks himself, and knew this for the hailing-salute of the Western Regions armies, meaning: nine deaths, and no regret.",
# L51
"But what could this signify? Chen Xuanli retorted without the least mercy: 'To blast apart the Taishang Xuanyuan Lantern-Tower, to set fire to the Qinzheng Wuben Tower, to butcher a prince of the blood, to carry off the Son of Heaven, is this your so-called peace and safety?'",
# L52
"'General Chen, if I told you that all I have done from yesterday to today has been in the discharge of my duty as a Commander of the Jing'an Bureau, in a desperate striving to prevent these very things, would you believe it?'",
# L53
"Chen Xuanli, past all anger, laughed instead: 'Before the eyes of the whole multitude you hailed the aphids as your sworn brothers, and now you speak such ghost-talk, do you take us all for children of three?' Feng Dalun barked too: 'When you first killed the Wannian County lieutenant, I knew you for a base wretch given to slaughter and past all decency. Now, by good luck, you have hoodwinked your superiors and fobbed yourself off with the rank of a Commander of the Jing'an Bureau, and instead of thinking to repent, you grow worse than ever. Only at death's door do you bethink you of fabricating lies to beg for your life. Do you truly take us all for blind men?'",
# L54
"Every phrase of his fastened tight upon the charge, a knife-and-brush clerk's own keen craft indeed. Even Chen Xuanli, hearing it, nodded faintly.",
# L55
"Zhang Xiaojing heaved a sigh, knowing how very hard it was to make these things clear. The people about him would not understand his plight, still less grasp how cruelly hard a choice he had made this day.",
# L56
"Those who could have borne witness to Zhang Xiaojing's struggles within the lantern-tower, Yuchang, Xiao Gui, and the whole band of aphids, were all dead and gone, every one. Only Taizhen and Tanqi could prove his innocence at second hand, and would they? Even were they willing, would the Son of Heaven believe it? Even if the Son of Heaven believed it, would the court make it known?",
# L57
"Zhang Xiaojing knew the temper of these people all too well. After so great and shocking a calamity as this day's, the court must find a chief culprit, so as to render some account to every quarter and keep up its own countenance. With Xiao Gui dead, the best choice for them was to fling out Zhang Xiaojing as the scapegoat, however well they knew in their hearts what he had done.",
# L58
"From the Son of Heaven at the top down to Feng Dalun at the bottom, they would push this thing through without a moment's hesitation. Zhang Xiaojing could not for the life of him think what way of deliverance there was left to him.",
# L59
"The great city of Chang'an was for all the world like a raging monster, foredoomed to devour the very guardian who stood nearest it. He who would save it must bear the city's own misprision and be its sacrifice.",
# L60
"Zhang Xiaojing lifted his head, looked up at the sky, as clear as at this same hour yesterday, and a trace of a smile came to his lips. He flicked the dust from the socket of his eye, lowered his head, and looking at Chen Xuanli said slowly: 'So be it. A man must in the end answer for his own choices. I will tell you, then: the aphids are dead to the last, and the Son of Heaven and the Daoist Taizhen are safe and sound.'",
# L61
"'Where are they?'",
# L62
"'First let these two go, and then I will speak.'",
# L63
"Zhang Xiaojing pointed to Wen Ran and Cen Shen, and put on an air wholly open and aboveboard. Since the end was foreordained, he had given up pleading his own case, and asked only that they two might get away in safety.",
# L64
"But again Feng Dalun leapt out: 'General Chen, do not believe him! This fellow's ways are cruel and his heart harbors mischief! To come out with such words all of a sudden, there must surely be some plot behind it!'",
# L65
"Chen Xuanli stared at the wholly composed Zhang Xiaojing, somewhat at a loss what to do. Just then Prince Yong of a sudden spoke: 'Let my father the Emperor's safety weigh first.'",
# L66
"Chen Xuanli and Feng Dalun were both astonished. For the prince to say so was as good as agreeing to let Wen Ran and Cen Shen go. But this reason of his sprang from pure filial piety, and no one dared oppose it.",
# L67
"So Chen Xuanli made a few signs, bidding the soldiers open a lane. Wen Ran let out a shrill and piteous cry: 'Benefactor, you cannot cast me off alone! I will not go!' and clung fast to his arm. Zhang Xiaojing stroked her head with tender pity and charged her: 'This is all the flesh and blood our Eighth Company has left; live on well for our sakes.'",
# L68
"Even as he spoke, he reached out a hand and struck sharply at the side of Wen Ran's neck. Wen Ran gave a small moan and fainted away.",
# L69
"Zhang Xiaojing said to Cen Shen: 'I must trouble you to take her away; I have brought you much grief today.' This time Cen Shen dared play the hero no longer; he knew that if he did not go now, some vast trouble would come of it, and so, in silence, he propped Wen Ran up and started outward.",
# L70
"Feng Dalun was a little unwilling; but on second thought: first do Zhang Xiaojing to death, and as for Wen Ran, so long as she stayed within Chang'an, need he fear that the Bear Fire Gang would want for chances to torment her by and by?",
# L71
"Cen Shen, bearing Wen Ran up, walked slowly down the lane the Longwu soldiers had opened. The soldiers to either side wore looks of savage menace, and Cen Shen could only hold his chest as straight as he might and press down the disquiet within him. Halfway along he suddenly looked back, and saw Zhang Xiaojing still standing bolt upright where he was, his two hands spread wide, that single eye fixed all the while upon this quarter.",
# L72
"Out of a poet's sensitivity, he had a strong feeling: Zhang Xiaojing had already set his mind on death. The moment Wen Ran passed from his sight, the last thread binding him to this world would snap, and thenceforth he would cling to nothing. Cen Shen knew this man but little; yet from his slight acquaintance with Wen Ran, Yao Runeng, and a scant few others, he knew he was by no means the base and murderous villain Feng Dalun made him out. The story behind him was, he feared, as deep as sunken hills and heaped-up seas.",
# L73
"He let out a deep, deep sigh. A hero at the end of his road, sorrowful and forsaken, this was matter of the finest for a poem. But alas, the poet's good fortune was not the hero's; the fierce emotion within his breast was near to bursting him open.",
# L74
"At that very moment a golden gong sounded far off, its beat urgent. All at once the attention of everyone before the Yixiang Pavilion was drawn to it. They saw the flags flying on a distant watchtower, and not on one alone; the watchtowers on every side were passing the selfsame message, until the whole sky over Chang'an was all but filled with it.",
# L75
"One who knew the flag-code read it off at once and reported to Chen Xuanli: 'The Son of Heaven is unharmed.' Chen Xuanli was at once amazed and overjoyed, and hastily asked for the particulars; but the watchtower had not yet had time to furnish anything more detailed, and it was known only that the word had come from the direction of the Yanxing Gate.",
# L76
"Feng Dalun shot a glance at Zhang Xiaojing, his face all delight. The Son of Heaven unharmed, this fellow had lost his last bargaining chip, and could now be butchered at anyone's will!",
# L77
"Zhang Xiaojing smiled faintly and bitterly. It was he who had sent the word to the Yanxing Gate, and he had never thought that this well-meant act would become the death-warrant of himself and two others besides.",
# L78
"But he was helpless.",
# L79
"'Deputy Director Li, that matter I can no longer tell you; but I have at least kept my promise.' Zhang Xiaojing murmured to himself, closed his eyes, and, facing the sharp arrowheads, drew up his chest and walked forward.",
# L80
"Feng Dalun had no wish at all to leave him alive. The moment he saw Zhang Xiaojing's frame stir, his eyes rolled, and he shouted at once at the top of his voice: 'Look out! The prisoner means to flee!'",
# L81
"The Longwu soldiers' spirits were strung to the highest pitch; hearing this all of a sudden, with a whir they raised their crossbows by instinct and were on the point of loosing the triggers at Zhang Xiaojing.",
# L82
"In that hair's-breadth instant, a voice all at once came flying from behind the crowd:",
# L83
"'Hold!'",
# L84
"'An Lushan?'",
# L85
"The name was quite strange to Li Bi. The squad leader hastened to add a word of explanation: 'He is a mongrel Hu of Yingzhou, the adopted son of General Zhang Shougui.'",
# L86
"At the word Hu, a sharp light came into Li Bi's eyes. For a Hu to be a military commissioner was no great rarity in the great Tang, yet neither was it common. That An Lushan had risen to such a post showed that he had no small skill at pushing his own fortunes. But still, this fellow was no more than a newly appointed military commissioner of Pinglu; how did he dare to raise so great a matter in Chang'an itself? It was bold to the point of absurdity. Li Bi felt all along that the thing would not stand to reason; there must be some further crook in it.",
# L87
"'Where is the Pinglu resident-agent courtyard? Take me there.' Li Bi strode toward the door. The squad leader, unwilling as he was, saw the murderous air about him and could only follow along, sullen and grudging.",
# L88
"Across from the Shouzhuolang's stronghold stood the ten resident-agent courtyards. This was where the military commissioners of every region kept their eyes and ears in the capital and carried on their daily business; ordinarily it was a district all to itself, into which the Chang'an authorities could not reach. But today a body of Lüben Guards had all at once appeared in the streets and lanes, bearing down upon the place with a threatening air, and startling not a few eyes in the shadows.",
# L89
"The people here were well informed of all that passed in the capital, and at the sight of this troop could not but call to mind that great upheaval at the Xingqing Palace. So they exchanged glances of doubt, yet none dared make a sound.",
# L90
"Led by the squad leader, Li Bi brought his men straight to the third courtyard on the western side. At the very center of this resident-agent courtyard there flew a blue-dragon flag with a black border; blue belongs to the east, the black border to the north, which answered exactly to the bearings of the Pinglu command.",
# L91
"A Lüben guard-soldier went up to the gate and beat upon its boards with a bang-bang; and before long there came out a middle-aged man in a brown robe. He was thick of brow and short of eye, with much of the soldier's bearing about him, yet when he smiled it was like a smooth and worldly merchant. The moment he opened the gate, before Li Bi could speak, he made a deep bow and cried that he deserved ten thousand deaths.",
# L92
"Li Bi had pictured beforehand all manner of reactions from the Pinglu resident-agent courtyard, but had never thought it would be like this. He knit his brows, at a loss what to say. The middle-aged man had already straightened up, and with a smiling face announced who he was.",
# L93
"It turned out his name was Liu Luogu, the man in charge of this Pinglu resident-agent courtyard in the capital, and a confidant of An Lushan's. At the word Li Bi at once put away his contempt. This manager, from the doings of the officials at the top down to the traffic in money and grain at the bottom, pried into everything; his hand and eye reached to the very heavens, and though he held no office his power was not to be made light of.",
# L94
"Li Bi said coldly: 'You cry that you deserve ten thousand deaths; does that mean you knew my errand all along?' Liu Luogu, his face still wreathed in smiles, said only two words: 'Consignment-sale.'",
# L95
"At those two words, Li Bi's face darkened.",
# L96
"The court officials of the great Tang were forever entangled in certain large transactions that could not decently be made public. To avoid trouble they would often entrust some rich merchant to act for them, all receipts and outlays running through the shop's own account-books, and this they called 'consignment-sale.' In time the resident-agent courtyards of the several regions began to take on this kind of business too: being government offices, they ran no risk of bankruptcy; and since a military commissioner held both military and financial power in his own hand, so that outsiders could hardly meddle, the secrecy was a degree deeper still.",
# L97
"At this word from Liu Luogu, Li Bi understood at once. The accounts the Shouzhuolang had settled through the Pinglu resident-agent courtyard were in truth the consignment-sale of some great personage at court. This great personage had hired the Shouzhuolang somewhere outside the capital, but the cost had gone through the books of the Pinglu resident-agent courtyard. Thus the hiring of men ran outside the capital and the entering of accounts within it, the men and the money two separate threads. However the thing was turned about, this great personage could keep himself hidden clean away from it, steady as a mountain.",
# L98
"The one thing he had left out of his reckoning was that Liu Luogu should sell him out so readily as this...",
# L99
"Li Bi asked that very question: 'Why do you sell out your consignment client so readily?'",
# L100
"Liu Luogu said with a grave face: 'The way of the consignment-sale sets great store by good faith. This courtyard never inquires into what use a client makes of his money; yet should it perceive any doing of wrong or breaking of the law, it has the duty besides to lay information before the court. Last night, meeting so sudden an upheaval, we were sore afraid, and the courtyard must needs look into itself and search itself over. Commissioner An is deep beholden to His Majesty's grace, and often admonishes his people to be loyal and to bear the state at heart, to spend their toil for the Son of Heaven; were he in the capital, he too would approve my doing thus.'",
# L101
"High-sounding as his words were, Li Bi caught their drift: this was to shrug the resident-agent courtyard's liability off elsewhere, and to hint besides that An Lushan knew nothing of the matter, and that, standing in the imperial favor, he was not to be probed too deeply. This Liu Luogu was an old hand indeed: well informed, needless to say, and, at the first whisper of the wind, at once fully prepared, showing with hearty readiness the posture of one wholly willing to cooperate.",
# L102
"Li Bi did not, in truth, think An Lushan a party to it: a mongrel Hu off in some remote and out-of-the-way place, what great stir could he raise? What he most urgently wished to know now was who this great personage of the consignment-sale might be. But Liu Luogu shook his head: 'The consignment-sale is a secret business; the identity of the great man is kept hidden even from us. Yet the accounts may show a thing or two.'",
# L103
"So saying, he produced an account-book. This ledger was no ordinary bound scroll, but yellow hemp-paper of Shu Prefecture cut into leaves an elbow's length long, laid one over another and strung together with fine cord, of a length to be bound behind the elbow and consulted at any moment on the road. At a glance at its make, Li Bi knew it could be no forgery.",
# L104
"It was a master-ledger, recording only the gross sums in and out, with no itemized entries. Liu Luogu said that they settled payments only as the client directed, and how the money was spent they did not care; but for Li Bi it was enough.",
# L105
"For it must be understood that, from the Türk Wolf Guards to the aphids, from the fierce-fire oil to the Que-le Huo-duo, this was a plan of the vastest scale. The food and lodging and travel of close upon a hundred men, the safe-houses, the workshops, the buying and moving of materials and gear and carts and horses, the bribes to smooth every joint of every government office, the fees for gathering intelligence and for papering over every flaw, the outlay at each single link in the chain was, one may say, a staggering figure.",
# L106
"So costly a plan could never have been borne by that pack of poor, down-at-heel discharged old soldiers, the aphids. This was one of the reasons Li Bi had all along believed there must be someone else behind them.",
# L107
"The dealings between the Shouzhuolang and the Pinglu resident-agent courtyard in the second year of Tianbao came to more than ten thousand strings of cash, of which the capital's own expenditure was but two thousand strings. In other words, if there were some eight thousand strings of receipts and outlays in this master-ledger, in all likelihood they were the work of that mysterious consignment-man.",
# L108
"Liu Luogu and Li Bi soon found this very entry: eight thousand six hundred strings exactly, paid off at a single stroke, in the eighth month of the second year of Tianbao.",
# L109
"In the ninth month of the second year of Tianbao, the Shuofang resident-agent courtyard sent word for the first time that the Türk Wolf Guards were stirring. In the same month the Jing'an Bureau was established, drawing men across every office and bureau. In point of time it tallied exactly with this one payment.",
# L110
"Li Bi's gaze grew keen. The runner of the main hall had, most likely, wormed his way into the Jing'an Bureau at just that time; every clue tallied to a nicety.",
# L111
"A blade of wrought steel, two strings; a privately forged crossbow-lock, eight strings; a Türk post-horse, thirty-nine strings. Such were the current market rates. These eight thousand six hundred strings would, barely and with a squeeze, meet the plan's everyday costs. The consignment-man might have had other outlays besides, but they would not have run through here.",
# L112
"At the back of the account there were appended some notes besides. Liu Luogu said that a consignment-man was generally unwilling to show his true self, and would commonly agree with the resident-agent courtyard upon a place of delivery and a secret sign of contact, set down after the accounts. Li Bi said nothing, but bent his head and ran his eye over them, and all at once his gaze halted upon four characters.",
# L113
"This was the meeting-place fixed each time between the resident-agent courtyard and this consignment-man:",
# L114
"'The Shengping physic garden.'",
# L115
"There was only one physic garden in Shengping Ward, and that was the physic garden of the Eastern Palace.",
# L116
"Li Bi silently closed the ledger and handed it back to Liu Luogu. Liu Luogu, well used to reading men's faces, saw that this fierce-tempered Deputy Director of the Jing'an Bureau beside him had all at once drawn in his edge and gone deathly dull. He asked with concern: 'Is there aught else the Deputy Director would have this humble courtyard do?'",
# L117
"'There is nothing more.'",
# L118
"Li Bi answered listlessly. The surmise he had all this while so strenuously shunned had become a fact hard and cruel as iron. His fingers trembled faintly, and a blankness came over his eyes. Deep-laid schemer though he was, before this turn of events he knew not what to do.",
# L119
"Just then a clear ringing of a gong came to him: a watchtower was about to pass some weighty message. Li Bi looked up by instinct, and when he made out the flag-signal, his whole body gave a violent shudder, as though thunderstruck.",
# L120
"'The Son of Heaven is unharmed!'",
# L121
"Liu Luogu had marked the message too, and was about to put a question to Li Bi, when to his astonishment he found that the man was already gone.",
# L122
"A rapid patter of footsteps rang out through the resident-agent courtyard: Li Bi ran out at a speed never seen in him before, vaulted onto his horse, and was off at the crack of a whip. The Lüben soldiers nearby stood rooted where they were, watching him gallop away in a trail of dust, and looked at one another, at a loss.",
# L123
"With no instruction and no charge given, the master of the Jing'an Bureau had left them, thus, past all understanding.",
# L124
"On horseback Li Bi gripped the reins, past all care for anything now; he had but one goal, the physic garden of the Eastern Palace, the physic garden of the Eastern Palace where the heir apparent was.",
# L125
"That cry of 'Hold!' had come in time to check the Longwu soldiers in the very act of loosing. Had it come half a finger-snap later, Zhang Xiaojing would likely have been shot into a sieve.",
# L126
"Chen Xuanli, Prince Yong, and Feng Dalun alike turned toward the sound. They saw a broad-browed official making his way through the crowd, hurrying toward them, and walking with a limp besides. His clothes were all smeared with soot; a glance showed him for another survivor of the Qinzheng Wuben Tower. Close behind him followed a beautiful woman with a veil over her face.",
# L127
"Chen, Feng, and Prince Yong called out his name at the same moment: 'Yuan Zai?'",
# L128
"Yet the three said it in somewhat different tones. Prince Yong's was indifferent, taking him for no more than a common official; Chen Xuanli's held, within its disdain, a few threads of approval, for it was Yuan Zai's timely report of the military situation that had let the Longwu Army enter the Qinzheng Wuben Tower at the first instant; while Feng Dalun's tone was half warmth and half delight.",
# L129
"It was thanks to this fellow's deft hand earlier that Feng Dalun had got clear of the guilt of wrongly seizing Wang Yunxiu, and had driven Zhang Xiaojing to the wall. Now that Yuan Zai had appeared here of a sudden, he could drive one more firm nail into an already all-but-certain case.",
# L130
"Though he did not know why the man should call off the bolts aimed at Zhang Xiaojing, yet with this fellow's cunning he must surely have hit on some better and more venomous device. So thinking, Feng Dalun spread his arms with a face all smiles and came warmly forward to meet him. But Yuan Zai raised a hand to bid him wait; Feng Dalun took the hint in a flash and hastily drew back, not forgetting to steal a glance at Zhang Xiaojing, the one-eyed Yama still standing where he was, hands bound, awaiting death.",
# L131
"Yuan Zai first made a bow apiece to Prince Yong and Chen Xuanli, then opened his mouth and said without expression: 'I come, on behalf of the Jing'an Bureau, to take into custody the chief culprit of the lantern-wheel affair.'",
# L132
"This move surprised no one. Zhang Xiaojing had been, after all, a Commander of the Jing'an Bureau, and his defection was a vast stain; if the Jing'an Bureau did not make the arrest itself, it stood to lose every shred of face, within and without.",
# L133
"At some unnoticed moment a pair of cast-iron manacles had appeared in Yuan Zai's hand, clanking as they swung. He stepped forward and dropped the manacles over the other's head, and the chain slid neatly off both shoulders to wind about the wrists.",
# L134
"'The net of the law is vast; wide-meshed, yet it lets nothing slip!' Yuan Zai cried out in high righteousness.",
# L135
"All present, Zhang Xiaojing among them, were startled: for Yuan Zai's manacles had, of all things, been hung about Feng Dalun's head.",
# L136
"'Gongfu, what are you doing?' Feng Dalun cried in alarm, struggling to twist free of the manacle-chain. Yuan Zai said coldly: 'Your plot is laid bare; you need play the hypocrite no longer.'",
# L137
"'You're mad! The chief culprit is that Zhang Xiaojing!' Feng Dalun cried, alarm and fury together.",
# L138
"At this Chen Xuanli could not help frowning: 'Yuan Zai, what is your meaning? Can it be that this Feng Dalun is Zhang Xiaojing's confederate?' Yuan Zai shook his head: 'No. This fellow is the hidden master behind the aphids; and Zhang Xiaojing is a Commander of the Jing'an Bureau, mine own; he never turned traitor, but only went under cover among the aphids.'",
# L139
"'Absurd!' Chen Xuanli flew into a violent rage. 'He assaulted the palace guard and carried off the Son of Heaven, and all before the eyes of the multitude; do you take me for a blind man?!' He clapped his hand hard on his sword-hilt, ready at any moment to whip out the blade and cut down this treacherous fellow.",
# L140
"A flicker of fear passed across the depths of Yuan Zai's eyes, but was gone as soon as shown: 'That was to win the aphids' trust; he did it of necessity, having no other way.'",
# L141
"'What proof have you for it?!'",
# L142
"Yuan Zai smiled: 'I have a witness who can resolve General Chen's doubts.'",
# L143
"'Who? And why should I believe a word he says?'",
# L144
"'This man's word you will surely trust.' Yuan Zai turned his head and made a deep bow to Prince Yong. 'His Highness Prince Yong.'",
# L145
"Prince Yong had all this while held his head aslant, his face none too pleasant. But at Yuan Zai's appeal he hesitated again and again, and at last, with no great willingness, spoke to Chen Xuanli: 'Just now in the Star-Plucking Hall, Zhang Xiaojing made a feint of pushing me down; in truth it was to give word to Yuan Zai to bring down the tower-within-the-tower.'",
# L146
"It dawned on Chen Xuanli: no wonder the Star-Plucking Hall had collapsed so suddenly, no wonder Prince Yong had come out alive from under Zhang Xiaojing's hand; so this was the reason of it.",
# L147
"Prince Yong bore Zhang Xiaojing a deep grudge; since even he said so, the thing seemed to be true. Thinking thus, Chen Xuanli cast another glance at the prince's face, and his heart was clear as a bright mirror. Had Yuan Zai not come, this prince would likely not have stood forth of his own accord to bear witness, but would only have watched Zhang Xiaojing die.",
# L148
"And the more this was so, the more it proved Yuan Zai's words no lie.",
# L149
"'Then his carrying-off of the Son of Heaven...' Chen Xuanli asked again.",
# L150
"Yuan Zai explained at his ease: 'The aphids were then in great force; Zhang Xiaojing could not break in among them, and could only follow along with the rebels and bide his chance to strike. Now that the Son of Heaven is unharmed, does that not go to show that he is loyal still to the great Tang? I believe that, when presently we come before His Majesty, the whole truth will be made plain.'",
# L151
"His words dovetailed so exactly with Zhang Xiaojing's own defense a moment before that others could not but believe. Chen Xuanli could only wave a hand, bidding the soldiers lower their crossbows first, to avoid any hurt by mischance.",
# L152
"At this the manacled Feng Dalun let out a heart-rending roar: 'Even if Zhang Xiaojing never turned traitor, what has that to do with me!' Yuan Zai turned his face slowly toward him, a cold smile upon it, nothing like the warmth of their first meeting.",
# L153
"'Zhang Luo, recorder of the Forestry and Crafts Bureau, are you acquainted with him?' Yuan Zai asked all at once.",
# L154
"Feng Dalun was taken aback a moment, then nodded. This was a colleague of his; both were recorders of the Forestry and Crafts Bureau, only Zhang Luo had no arts of maneuver, and his standing was far lower. Which was why the charge of the lantern-fair watch had been pushed onto Zhang Luo's head.",
# L155
"Yuan Zai said: 'Just a few double-hours before the lantern-tower was lit, he was, past all explaining, shoved off an arched bridge, and whether he lives or dies is unknown. I have questioned the Longwu men on watch: the bamboo passes used by the artisans who entered the lantern-tower were all issued under your signature.'",
# L156
"At this Feng Dalun grew frantic. The recorders of the Forestry and Crafts Bureau were few and their paperwork heavy, so that recorders of equal rank would sometimes sign for one another, nothing more ordinary. Feng Dalun would have wagered that, if the artisans' bamboo passes into the lantern-tower were examined with care, several recorders' names would surely be found on them, and even the countersignature of the Bureau's vice-director besides; it was by no means he alone.",
# L157
"But the way Yuan Zai now framed his words, anyone hearing them would take it that Feng Dalun had killed Zhang Luo and then issued the aphids their bamboo passes, that they might slip into the lantern-tower. Before Feng Dalun could open his mouth to plead, Yuan Zai cut across him: 'Without the collusion of someone within the Forestry and Crafts Bureau, how could the rebels have brought off so great a thing?' The retort held nothing of substance, yet to the ears of the crowd Feng Dalun had become, as it were, the rebels' mole hidden within the government.",
# L158
"'This is slander!'",
# L159
"'You strove so hard just now to name Zhang Xiaojing a rebel, was that not to frame a loyal and worthy man?' Yuan Zai retorted with a pointed edge. Feng Dalun blurted out: 'I want him dead, and that is because...' and there he stopped short.",
# L160
"'Because of what?' Yuan Zai narrowed his eyes and pressed the question at his leisure; but Feng Dalun dared say no more.",
# L161
"To say more would inevitably drag in last year's affair of the Wen Incense Shop, and the little maneuver of yesterday, when Prince Yong had set Yuan Zai on to frame Zhang Xiaojing. Feng Dalun cast a glance at Prince Yong, saw his look was far from kind, and knew that if he brought the matter out, the end would likely be more wretched still.",
# L162
"Feng Dalun was near to madness. How had Prince Yong and Yuan Zai turned enemies all at once? Was not the doing-to-death of Zhang Xiaojing in the interest of everyone? The three of them had plainly been in the same boat; how had it capsized at a word?",
# L163
"All of a sudden he ran up before Chen Xuanli, dropped to his knees with a thud, and wailed aloud: 'General Chen, you see it all clearly, it is plainly that villain Zhang Xiaojing who has hoodwinked Prince Yong; you must not lightly believe another man's word!'",
# L164
"Chen Xuanli half believed and half doubted. In feeling, he could have wished Zhang Xiaojing dead on the instant; but in reason, Yuan Zai's account had much sense in it. He pondered a moment, then spoke to Yuan Zai: 'Have you any other proof?'",
# L165
"Yuan Zai gave a slight smile and stepped aside; the veiled woman behind him came forward before them all. She slowly drew off the veil, showing a fair and comely face, none other than Wang Yunxiu, daughter of Wang Zhongsi. Chen Xuanli had heard a little of her misfortunes, and knew she had lately been abducted by the Türk Wolf Guards and, saved by Yuan Zai, had by good luck got away home.",
# L166
"Yuan Zai said to her with all deference: 'Mistress Wang, I know that you were rudely used by the rebels today, and that your spirit can ill bear deep disturbance. But this matter touches the safety of the court, and I must trouble you, against your will, to come once more to the old place and identify the villain. If there be aught wanting in my consideration, I beg your pardon again beforehand.'",
# L167
"A faint flush rose in Wang Yunxiu's cheeks, and she said softly: 'Yunxiu is but a woman, yet she too knows that affairs of state must weigh first. Order it all as you will.'",
# L168
"Those about them were mystified, not knowing what it meant that Wang Yunxiu should pop up so abruptly. Only Feng Dalun's face grew more and more wretched, his lips quivering, his body unable to stir.",
# L169
"Yuan Zai brought Wang Yunxiu to the firewood shed beside the Yixiang Pavilion, pushed open the door, and asked her to go in and look about. Wang Yunxiu had not been in long before she came out trembling all over, and said in a low voice: 'That is right, this is the place; after I was seized, it was here I was thrown...'",
# L170
"At these words Chen Xuanli's eyes changed at once, and when next he looked at Feng Dalun it was with a face full of loathing.",
# L171
"Wang Yunxiu had been abducted by the Türk Wolf Guards, and had, of all things, been kept in the firewood shed beside the Yixiang Pavilion. What this meant needed no spelling out. Between the Türk Wolf Guards and the aphids there had all along been a tie past clear telling; set beside the fate of Zhang Luo, recorder of the Forestry and Crafts Bureau, and the issuing of the bamboo passes, the truth all but leapt forth, the proof conclusive.",
# L172
"Feng Dalun's eyes started round; he could have burst with rage. The seizing of Wang Yunxiu had been a mere blunder, and Yuan Zai had even helped to cover it over for him; who would have thought the fellow would turn his hand about and make of it iron-clad proof of collusion with the Türks?",
# L173
"Feng Dalun would have argued on, but found he knew not how to begin.",
# L174
"The several matters Yuan Zai had set out were, in truth, either blunders or ambiguities, with no connection among them. Yet he had, of all things, the art to make everyone believe them a tight and rigorous chain, proving to perfection that Feng Dalun was a traitor, who had first helped the Türks abduct a great minister's kinswoman and then secretly aided the aphid artisans to steal into the lantern-tower, so that every evil deed was, well-nigh, his alone.",
# L175
"He remembered, too, how, when Yuan Zai had earlier framed Zhang Xiaojing, he had laid out a few pieces of proof, nailed fast to the board, that had won his boundless admiration. Who would have thought that a few double-hours later he would set out a few more pieces of proof and reach a wholly opposite, yet equally convincing, conclusion?",
# L176
"Feng Dalun began full of wrath, but the more he thought the more his heart quailed, until at last a boundless chill wrapped him round. A turn of the hand brings cloud, a turn back brings rain. Proof in Yuan Zai's hands was for all the world a lump of yellow clay, to be pinched into whatever shape he pleased. Could it be that Lai Junchen's Classic of Entrapment had fallen into his keeping?",
# L177
"'A servant of the court, and yet you formed a society and a faction within the walls of Chang'an, and gathered the young and stout in secret, all for this day's work, I dare say?' With this last, Yuan Zai drove one more nail into his coffin. That single sentence all but settled the fate of the Bear Fire Gang.",
# L178
"'I am wronged! He is slandering me! Prince Yong! Prince Yong! You know the truth!' Feng Dalun, past all restraint, screamed hoarsely at Prince Yong; only Prince Yong could save him now.",
# L179
"Prince Yong was unmoved. The affair of the Wen Incense Shop had, when all was said, been a mess that Feng Dalun had stirred up for him; to be rid now of this odious fly was well enough.",
# L180
"Chen Xuanli, seeing Prince Yong's attitude, understood at once. He flicked a finger, and several soldiers came forward, kicked Feng Dalun sprawling to the ground and beat him savagely, and fetched a stick of firewood from the shed to stuff into his mouth and keep him from making any sound.",
# L181
"The moans of pain soon sank low. Feng Dalun lay grovelling on the ground, his face all blood and filth, curled up like a shrimp. This recorder of the Forestry and Crafts Bureau raised one hand, as if crying to someone for rescue, but soon it drooped limply down again.",
# L182
"Chen Xuanli felt not a jot of pity. After last night's great calamity, the court needed someone it could put to death in public; if not Zhang Xiaojing, then this Feng Dalun would do. The proof was enough for now; though some doubtful points remained, there was no need to probe them deep.",
# L183
"Yuan Zai watched Feng Dalun struggle with a smile, as one savoring a finely wrought vessel of Persian gold; fortune stood, sure enough, on his side yet. Henceforth the whole of Chang'an would know that, when the lone and dauntless hero who had saved the Son of Heaven was being framed, an upright petty official had spoken out for justice, and had in the end helped clear the hero of his wrong and see justice done.",
# L184
"In the crowd not far behind him, Tanqi, a bamboo rain-hat on her head, wore a look of relief, yet in her eyes there lay a deep dread.",
# L185
"In fact they had reached the neighborhood of the Yixiang Pavilion long before; and Tanqi, seeing the three of them, Zhang Xiaojing, Wen Ran, and Cen Shen, hemmed in, had urged Yuan Zai in haste to go over and explain. But Yuan Zai had held her back, saying the moment was not yet come, and bidding her wait. Only when Zhang Xiaojing was on the very point of being shot down, and the watchtower passed its urgent word, did Yuan Zai go over, and, plying his glib and reedy tongue, retrieve the whole situation.",
# L186
"Tanqi had not understood at first why Yuan Zai said the moment was not yet come; now, all at once, she saw it.",
# L187
"He had been waiting, waiting for the word that the Son of Heaven was unharmed.",
# L188
"Yuan Zai hated Zhang Xiaojing so bitterly, yet could turn his stance about and come gladly to his aid, purely because the act would win the Son of Heaven's trust and gain him vast advantage; had anything befallen the Son of Heaven, to do so would have been meaningless, nay, harmful.",
# L189
"So the moment he had been waiting for was the Son of Heaven's fate. Let the Son of Heaven live, and Yuan Zai was Zhang Xiaojing's savior; let the Son of Heaven die, and Yuan Zai was Zhang Xiaojing's executioner.",
# L190
"This Yuan Zai could, of all things, shift back and forth between two utterly opposite stances with perfect ease, without the least hitch. When Tanqi thought that, had the word come but one finger-snap later, this greatest of allies would in an instant have become the most dangerous of enemies, a chill ran through her whole body: what a fearsome profit-hunting beast this was.",
# L191
"'Human nature has ever sought profit and shunned harm; it may betray loyalty and honor, benevolence and virtue, but it will never betray its own interest. So long as this matter profits me, mistress, you need have no fear that I will turn traitor.' Yuan Zai's words beside the Longchi echoed once more through Tanqi's mind.",
# L192
"Just then a stir ran through the ranks of the Longwu Army. Tanqi hastily gathered in her thoughts, lifted her head, and saw that Zhang Xiaojing had, of all things, moved.",
# L193
"While Yuan Zai's tongue had run in full spate, Zhang Xiaojing had stood all the while where he was, keeping a strange silence. Only when Feng Dalun was seized did he seem to wake as from a dream: first he looked about him, then he set his feet in motion and, staggering, made his way outward.",
# L194
"The Longwu soldiers did not stop him; in silence they parted to open a lane, and stood at attention on either side.",
# L195
"Zhang Xiaojing's guilt was washed clean, and what he had done before stood, of course, confirmed. It needed no great stretch of fancy for a bystander to guess the perils and the sacrifices he had borne. What the court's stance might be none knew; but in the eyes of these soldiers, here was a hero to be held in awe.",
# L196
"His whole body was smeared with the blood Feng Dalun had stabbed out of him, and its lurid, mottled color traced out the other wounds upon his frame: some from the blast in the West Market, some from the scorching of the lantern-tower, some from the Türk Wolf Guards' torture, some the marks of grappling with the aphids. Layer upon layer they lay, crossing and recrossing this one body, a record of all the heart-stopping perils of the past twelve double-hours.",
# L197
"He was weak past bearing, and walked with a swaying, unsteady gait; only that single eye still burned bright.",
# L198
"'The hailing-salute!' Someone in the ranks shouted out, none knew who. With a rush, the soldiers on both sides raised their right fists at once and struck them together against their left shoulders. Chen Xuanli's and Prince Yong's faces were a study in mixed feeling, but to this all-but-presumptuous act they both kept silence.",
# L199
"Tanqi, watching this, could not keep the tears from streaming down her face. But she soon saw that something was amiss: Zhang Xiaojing was not walking forward at random, but coming straight toward her. Had this lecher, of all things, picked her out where she hid in the crowd? Tanqi was thrown into sudden confusion, and stood rooted where she was, at a loss what to do.",
# L200
"What did he mean to do? What was she to do? What would he say? How should she answer? A thousand thoughts filled Tanqi's mind in an instant, and, clever as she was, even she knew not now what was best.",
# L201
"Now Zhang Xiaojing came up before Tanqi, put out both hands, and seized her by the shoulders all at once, so that she could scarcely stir. In that instant Tanqi all but forgot even how to breathe.",
# L202
"'Lech—' Tanqi cried out softly in her embarrassment, but was at once roughly cut off.",
# L203
"'Deputy Director Li, where is Deputy Director Li?' Zhang Xiaojing's voice was a hoarse, parched rasp.",
# L204
"Tanqi started; she had not looked for this to be what he would say. Zhang Xiaojing asked again, and she hastily answered: 'I have already learned from the watchtower that the young master survived by good fortune and has taken the Jing'an Bureau in hand once more. But where he is now, that I do not...'",
# L205
"Zhang Xiaojing roared: 'Go and find out, quickly! And get me a horse!'",
# L206
"That single eye of his flickered with an extreme of anxiety. Tanqi dared not delay, but turned in haste and ran off to the watchtower of Jing'an Ward.",
# L207
"Cen Shen, escaped from the jaws of death, came over bearing Wen Ran. He had watched the whole course by which a man turned from a vicious and desperate state criminal into a hero, and his heart surged within him; he felt that if only someone would bring him brush and ink just now, nothing could be more perfect. But alas, Zhang Xiaojing paid him no heed at all, only turning his neck restlessly to look about on every side.",
# L208
"Xiao Gui's dying words were burning fiercely all the while in Zhang Xiaojing's heart, keeping him restless and uneasy, with no mind at all to attend to anything else.",
# L209
"Now Yuan Zai sidled up, patted him on the shoulder, his face all smiles: 'The main matter is settled, the true culprit removed; Commander Zhang has toiled hard, and may set his mind at rest and take a good sleep.'",
# L210
"'The true culprit is another man!' Zhang Xiaojing said without the least ceremony.",
# L211
"The smile froze on Yuan Zai's face. What in the world was this death-row convict saying? I spent such pains to wash you white and found a perfect hidden villain besides, and now you say it is another man?",
# L212
"Yuan Zai looked over that way: Chen Xuanli was directing the soldiers to search the Yixiang Pavilion, and Prince Yong had, at some unmarked moment, already left. He let out a secret breath of relief, gripped Zhang Xiaojing by the front of his robe, and growled low: 'You fool! Don't go making fresh trouble!'",
# L213
"The words were scarcely out when there came all at once a crisp, sharp crack.",
# L214
"Yuan Zai clutched his swelling, smarting cheek and stared, wide-eyed, scarce able to believe it. This fellow had, of all things, hauled off and slapped him full in the face, when he had but this moment saved him!",
# L215
"'This is on behalf of every man of the Jing'an Bureau.' Zhang Xiaojing said coldly.",
# L216
"Yuan Zai was about to flare up, but saw a sudden edge shoot from Zhang Xiaojing's single eye. On the instant Yuan Zai felt a warmth spread beneath him: that dread planted deep in his heart he could not, even now, be rid of. Yuan Zai backed off a few grudging steps to put some distance between himself and that baleful star, rubbing his face and thinking he must not let Wang Yunxiu see him in so sorry a plight.",
# L217
"Just then Tanqi came running up, out of breath: 'Word has come from the Pingkang Quarter, the young master may be making for the physic garden of the Eastern Palace in Shengping Ward!' And in her hand she led a tall, fine horse of a yellow-brown color.",
# L218
"No one knew where Li Bi was bound; only Liu Luogu guessed that it had to do, most likely, with the place-name last mentioned. This guess was soon fed back to all the watchtowers. It was daylight now, and the common folk were all back within their wards, so that the roads and streets were empty of a soul. The watchtowers caught, with the greatest ease, the figure of Li Bi in his strange and headlong gallop.",
# L219
"Having this word, Zhang Xiaojing dragged up his weary body by force, gritted his teeth, and swung himself onto the horse. Tanqi would have gone with him too, but before she could speak Zhang Xiaojing had already given the horse a squeeze of the belly and galloped off, without leaving so much as a word behind.",
# L220
"Tanqi gazed off into the distance with a heart full of care; that swaying, unsteady figure looked as though it might fall from the horse at any moment.",
# L221
"From the Pingkang Quarter to Shengping Ward was four wards south; but from Jing'an Ward to Shengping Ward was only two wards east.",
# L222
"Li Bi had set out first, but Zhang Xiaojing had the shorter way.",
# L223 (opening vignette, recurs VERBATIM)
VIG,
# L224
"Two long neighs of the fine horses rang out; the two riders drew rein at the same moment, and looked each other level in the eye.",
# L225
"'Zhang Xiaojing?'",
# L226
"'Deputy Director Li.'",
# L227
"The looks on the two men's faces were not quite the same, yet in their eyes there seemed a thousand things waiting to be said.",
# L228
"Heaven was like some jesting player. The weather now was as clear and bright as when the two had first met, twelve double-hours before. Yet some things had changed, and forever.",
# L229
"Since Zhang Xiaojing had left the Jing'an Bureau at the Rooster hour, the two had met but once, and had had no chance at all to talk at length. Though neither knew just what the other had been through, they each believed that, without the other's striving, Chang'an would have worn a very different face.",
# L230
"The two had never been friends, yet were partners of the deepest unspoken understanding. Meeting again, they made no inquiries after each other's comfort; now was not the time for old acquaintance.",
# L231
"'I am going to the physic garden of the Eastern Palace; the heir apparent is the master behind it all.' Li Bi spoke plainly and to the point. His tone was very calm, but Zhang Xiaojing could see that his whole being, like the Taishang Xuanyuan Lantern-Tower, was about to burst into flame from within.",
# L232
"At that place-name Zhang Xiaojing's single eye flew wide of a sudden, and he all but fell from his horse. Li Bi shook the reins and was about to spur on, but Zhang Xiaojing stopped him.",
# L233
"'Do not go; it is not he.' Zhang Xiaojing's voice was withered and faint.",
# L234
"Li Bi raised an eyebrow; he knew Zhang Xiaojing would not say such a thing without cause.",
# L235
"'Before Xiao Gui died he left one sentence, a sentence that could throw Chang'an into chaos.'",
# L236
"'What was it?'",
# L237
"Zhang Xiaojing did not answer at once, but lifted his head and gazed toward the east. The bright sun hung high in the blue sky now, glorious and dazzling, and the whole hundred and eight wards of Chang'an were bathed in the mild sunlight of early spring. Against it, however splendid the lantern-wheels of the night before, they were become as humble and laughable as fireflies.",
# L238
"Li Bi followed Zhang Xiaojing's gaze. East of the Yongchong-Xuanping crossroads where they stood rose the Leyou Plateau, arching up over the due east of Chang'an. Broad and high it spread, covering the four wards of Xuanping, Xinchang, Shengping, and Shengdao; and the physic garden of the Eastern Palace lay in Shengping Ward, on the plateau's southern skirt. Spring had come, and the plateau was lush and green, and above all those rows upon rows of willows showed a vigorous green under the caress of the sun.",
# L239
"'One more breath of spring wind, and by the second month at the latest, the Leyou Plateau will be all green willow-shade.' Zhang Xiaojing said with a sigh.",
# L240
"'What is it you are trying to say?' Li Bi pressed, out of patience.",
# L241
"Zhang Xiaojing heaved a sigh, and slowly chanted two lines of verse: 'Who cut out these slender leaves, I cannot say— / the second month's spring wind is like a pair of shears.'",
# L242
"At the sound of it, Li Bi went rigid on his horse in an instant.",
# L243
"Green jade dressed up a tree grown tall, / ten thousand strands hung down in silken cords of green. / Who cut out these slender leaves, I cannot say— / the second month's spring wind is like a pair of shears. In Chang'an, from the oldest greybeard down to the smallest child, who did not know these lines for He Zhizhang's 'Ode to the Willow'? As a buliang chief of Chang'an, working cases in this literary capital where poets thronged, a man who knew no poetry would find it hard to get on. So the moment Xiao Gui chanted those two lines, Zhang Xiaojing had known at once whom he meant.",
# L244
"But the truth this laid bare was too staggering by far.",
# L245
"The Director of the Jing'an Bureau, charged with the security of Chang'an, was, of all people, the hidden master behind it all? How could such a thing be?",
# L246
"Zhang Xiaojing had half believed and half doubted it all along, taking it for no more than a venomous last device of Xiao Gui's, a wish to see Chang'an thrown into chaos before he died. But the moment he heard Li Bi say he was hurrying to the physic garden of the Eastern Palace, he knew at once that the thing was very likely true. Xiao Gui, at the point of death, had not deceived his brother.",
# L247
"'The physic garden of the Eastern Palace... the physic garden of the Eastern Palace... how did I never think of it? This has nothing to do with the Eastern Palace at all; it was plainly for the convenience of Director He.' Li Bi gripped the reins and murmured to himself on horseback.",
# L248
"The physic garden of the Eastern Palace lay in Shengping Ward, and the herbs it grew went first to the aged and senior ministers of the Eastern Palace's party. He Zhizhang's residence was set in Xuanping Ward, and the first thought behind it had been the convenience of fetching medicine from the physic garden—and, of course, the convenience of making contact with the resident-agent courtyard as well. Li Bi had been misled by those two words, 'Eastern Palace,' never thinking that the one most closely bound up with the place was, of all people, the Director of the Jing'an Bureau.",
# L249
"'To think... that behind it all should be Director He, of all men. What does he seek by it? On what does he presume?' Zhang Xiaojing could by no means make it out.",
# L250
"Thinking back now, He Zhizhang had indeed, within the Jing'an Bureau, put up no end of hindrances to Li Bi's doings. Each obstruction had its high-sounding reason; but, judged by its effect, it had greatly delayed the hunt for the Türk Wolf Guards.",
# L251
"But here there was one doubtful point that would not stand to reason.",
# L252
"'I remember that Director He was plainly already... er, sunk in a grave sickness and a swoon.'",
# L253
"Zhang Xiaojing looked at Li Bi with meaning.",
# L254
"On the fourteenth, at the hour of the Horse, second half, Li Bi, to gain control of the Jing'an Bureau, had used the death of Jiao Sui to vex He Zhizhang into illness and send him home to recover. Then at the Monkey hour, second half—that is, after Zhang Xiaojing had been taken by the Right Xiao Guard—Li Bi had gone to the Leyou Plateau to call on He Zhizhang, hoping to ask him to come forward and treat with the Right Xiao Guard, but had been refused.",
# L255
"What befell next in that bedchamber was murky and hard to make out.",
# L256
"The story given out was that He Zhizhang, hearing that the Right Xiao Guard had thwarted the Jing'an Bureau's work, had been seized with a rush of choler to the heart and fallen into a swoon; and that Li Bi had used this to coerce Gan Shoucheng and save Zhang Xiaojing. But Zhang Xiaojing knew that Li Bi's account held many doubtful points. He Zhizhang would never have taken his own safety so to heart; there could be but one reason for his sudden and unwaking swoon—Li Bi.",
# L257
"Mount Hua has but one road, and a great boulder blocks the way; whoever would climb it must clear away every obstacle.",
# L258
"'Are you sure he was truly in a swoon?' Zhang Xiaojing asked.",
# L259
"Li Bi marked the look in Zhang Xiaojing's eye, and said coldly: 'The Medicine King's yinyu wine is a marvelous prescription, yet one should not drink too much of it at a draught, or it will bring on, instead, the great wind-sickness.'",
# L260
"This was, in effect, to confirm Zhang Xiaojing's doubt at second hand.",
# L261
"A dreadful picture rose in Zhang Xiaojing's mind. He Zhizhang lay gasping on the bed, while Li Bi, medicine-cup in hand and face without expression, poured the yellow-brown decoction into him drop by drop, then pressed a pillow over his mouth and waited for the sickness to take hold. He Zhizhang's hands at first still flailed desperately, but little by little the strength went out of them...",
# L262
"'Are you sure he was not shamming to deceive you?' Zhang Xiaojing asked.",
# L263
"Li Bi nodded with full certainty. He was now like a wengzhong stone statue of an ashen face, without a spark of life in his whole body. After a long while Li Bi spoke slowly: 'I remember a question you once put to Yao Runeng: if a boat is in mid-river and a storm strikes of a sudden, and one innocent man must be killed to sacrifice to the river-god, that the rest may live, how should one choose? Your answer was: kill. And mine is the same.'",
# L264
"This speech of Li Bi's Zhang Xiaojing understood almost in an instant.",
# L265
"To save Chang'an, Zhang Xiaojing had sold out Xiao Yi, and in the lantern-tower had all but killed Li Bi; and Li Bi, for the selfsame reason, had laid his hand on He Zhizhang. For the sake of a more important end, these two men had each, without a backward look, chosen the road against all morality. But now, seeing the anguish in Li Bi's face, Zhang Xiaojing knew that the guilt he bore in his heart was no lighter than his own.",
# L266
"Both knew it well: this was a wrong that had to be done, yet a wrong is a wrong in the end. Every choice forced upon them dimmed their souls by one more degree.",
# L267
"'But...' Zhang Xiaojing knit his brows. 'If Director He was indeed gravely ill, how then is everything that came after to be explained?",
# L268
"A thick trace of self-mockery came over Li Bi's face: 'Perhaps Director He's plan was laid too perfectly—so perfectly that even were he to fall into a swoon midway, the plan would go off all the same. He had reckoned on everything, and only failed to foresee that I would so suddenly strike a blow so ruthless.'",
# L269
"At this he could not help a bitter smile.",
# L270
"The death of Jiao Sui, on the face of it, was Li Bi deliberately vexing He Zhizhang into flight; but in truth He Zhizhang had used the chance to act, finding a pretext to withdraw to his residence on the Leyou Plateau. He had meant to sit there and direct the plan that was to follow; but he never thought Li Bi would come calling of a sudden, still less that he would be so bold past all bounds as to lay a hand on him.",
# L271
"The successive misunderstandings of the two men grew into a most bizarre situation: the hidden master was done away with before the plan was set in motion, and yet the plan went on being carried out, step by orderly step.",
# L272
"It was an ironic thing indeed.",
# L273
"Li Bi and Zhang Xiaojing, seated on their horses, exchanged a few brief words. Before this the two of them had each had his own lot, and each had touched but one corner of the dark curtain. Now, meeting again, the broken tiles could at last be pieced into the shape of a whole relief.",
# L274
"He Zhizhang must have set down three chess-pieces within the city of Chang'an: one was the Türk Wolf Guards, one the aphids. The former to draw the eye aside, the latter to carry out the real plan. And there was a third: the traitor within, the runner of the Jing'an main hall, to work with the aphids at the needful moment and take one crucial step.",
# L275
"With He Zhizhang's standing and his arts, to make this whole train of arrangements without a sound was no hard thing.",
# L276
"'A while ago Director He sold off all his property in the capital, and we all took it that he was retiring to his home country to spend his wealthy old age; who would have thought he was pouring the money, through the Shouzhuolang, into the aphids here?' said Li Bi. Only so could it be explained how the aphids' power had grown to such a pitch.",
# L277
"'But...' Zhang Xiaojing still could not make it out. 'Why should he do such a thing?'",
# L278
"He Zhizhang had enjoyed literary fame for twenty years and more; in imperial favor, in renown, in office, all was brought to the full, and he had retired besides with the utmost pomp. An old man at the guttering end of his years—why should he run so desperate a risk and do a thing so monstrously against all right?",
# L279
"'Go and ask him straight out, then!'",
# L280
"Li Bi suddenly raised his whip and lashed the horse's rump hard. The startled mount leapt up and galloped off toward the Leyou Plateau. Zhang Xiaojing had foreseen he would react thus, and shook his own reins and followed after.",
# L281
"He Zhizhang had stayed all this while in his residence on the Leyou Plateau, and had not left it. Too much had happened this one day; whether he was truly in a swoon or no, the two of them needed to have it out with him face to face.",
# L282
"The night before, many great and noble folk had climbed the Leyou Plateau to view the lanterns, and both sides of the roads on the plateau were strewn with carelessly discarded scraps of food and bits of colored silk. Eight horse-hooves trod crossing and recrossing over this refuse, kicking up clouds of dust. The two riders never slackened, but made straight for Xuanping Ward in the northeastern corner. Along the way Zhang Xiaojing told, in passing, of the affair at the Yixiang Pavilion, but Li Bi offered no comment upon it.",
# L283
"Xuanping Ward was easy to find: one had only to make for where the willows grew thickest. It was the place with the most willows in the whole city, and had a byname, the Willow Capital. The two rode on a stretch, and saw from afar a luxuriant willow-wood; and half-hidden amid the green willows there could be seen an exquisite residence of black tiles and white walls.",
# L284
"The ground hereabouts was none too level, and by rights a horse coming here should have slowed. But Li Bi, as though gone mad, lashed his mount without cease to drive its speed higher, and bore straight down upon that residence.",
# L285
"Just then the great gate of the residence opened slowly, and a man came out from within. He seemed to have looked for these two riders all along, and stood in respectful welcome beneath the lintel, hands clasped.",
# L286
"The two riders drew nearer and nearer to the house, when all at once Zhang Xiaojing felt that something was wrong; he lifted his head and caught a disquieting smell in the air.",
# L287
"'Deputy Director Li, slow down!'",
# L288
"Zhang Xiaojing shouted aloud, but Li Bi turned a deaf ear and drove on madly, whip flying, and in a twinkling had passed through the willow-wood and made straight for the house. Zhang Xiaojing, seeing he could not catch up, swept his palm down in his anxiety and, without meaning to, touched something hard. He looked down: it was, of all things, a short crossbow hung at the side of the horse's belly.",
# L289
"The horse Tanqi had got for Zhang Xiaojing was from the string that rode with the Longwu Army, and its bridle and battle-gear had not yet been stripped off. Without hesitation Zhang Xiaojing took down the short crossbow, snicked a bolt into place, and pulled the trigger toward what lay ahead.",
# L290
"With a whistle the bolt flew out, crossed a dozen paces in a single finger-snap, and struck fast into the right side of Li Bi's mount. The horse gave a piteous cry and its forelegs buckled. Li Bi was flung all at once from its back and rolled, in an undignified sprawl, several times over on the ground.",
# L291
"Before Li Bi could grasp what had happened, Zhang Xiaojing had galloped up, leapt straight down from his horse, caught Li Bi in his arms, and rolled with him into an earthen pit at one side. His own mount, carried on by its fierce momentum, crashed with a roar into a willow tree, its sinews torn and its bones broken.",
# L292
"In the next instant, that tranquil residence amid the willows burst apart all at once; a scarlet fierce-fire bloomed out from within, spurting bright flame and broken tiles in every direction, and for a moment sand flew and stones hurtled, walls toppled and willows were snapped, and a violent firestorm rose up over the crest of the Leyou Plateau.",
# L293
"Who could have thought that hidden within this residence there was, of all things, a fierce-fire thunder of tremendous power?",
# L294
"Zhang Xiaojing pressed Li Bi's head down with all his might, holding him as close to the floor of the pit as he could, to keep clear of the shock-wave sweeping across. Sand and soil showered rustling down over their heads, and soon the two of them were buried under a thick layer of earth.",
# L295
"When all had grown still again, Zhang Xiaojing at last raised his head and shook the soil from the crown of it. The scene before him had changed utterly, heaven and earth overturned: the willow-wood was flattened, the rockery in ruins, and that once elegant and quiet residence upon the plateau was become a stretch of broken walls and toppled masonry, curling black smoke rising straight to the sky. As for the man who had waited before the gate, he too, of course, had been wholly devoured by that fire-beast and blown to powder and shards.",
# L296
"'Ha-ha-ha-ha...'",
# L297
"Zhang Xiaojing heard a strange peal of laughter. It came from beneath him, small at first, then louder and louder, until at the last it was near to madness. Li Bi lay at the bottom of the pit, his face all covered with mud, the muscles of it trembling ceaselessly amid the great laughter, so that the gray earth shifted into all manner of shapes, and his look was eerie.",
# L298
"'Be quiet!'",
# L299
"Zhang Xiaojing roared out savagely, dropped low, and looked warily about him. Never in the world had he thought that He Zhizhang would set a fierce-fire thunder even in his own residence; if the enemy had laid any further stroke in reserve, now was the time for it to come. But Li Bi shook his head: 'There will be no ambush now, none. I have seen it clear, seen it clear at last...'",
# L300
"'Why? Have you found out something more?' he asked.",
# L301
"Li Bi's laughter sank low, but then he said a thing past all understanding: 'Zhang Xiaojing, do you know why I, a man of the Daoist path, came back into the dusty world and took up the Jing'an Bureau?'",
# L302
"'For the heir apparent?'",
# L303
"Li Bi gave a slight nod: 'Just so. For the heir apparent I could sacrifice everything.' Then he paused, and his tone grew strange: 'And so was Director He.'",
# L304
"'What?' Zhang Xiaojing started at the word. What did this mean? Could it be that He Zhizhang was, after all, a loyal minister?",
# L305
"'Earlier I saw Li Linfu, and he said one thing to me—\"He who profits most is suspect\"—meaning that the one who stands to gain the most is forever the most to be doubted. Following that rule, I came to suspect that all of this was the heir apparent's doing. But now it seems I reckoned wrong... This gain need not be a gain in substance; it may also be loyalty.'",
# L306
"Zhang Xiaojing knit his brows tight, not understanding what he meant. Li Bi simply lay flat in the pit, his two eyes on the sky, and murmured:",
# L307
"'Before setting off the Que-le Huo-duo, the hidden master did two things. One was to make me show myself at the lantern-tower and lure the heir apparent away to the physic garden of the Eastern Palace—that you know. The other was, by a second letter, to send Li Linfu off to the residence in Anye Ward. The two left the spring banquet at the same time; what do you take his purpose to have been?'",
# L308
"Zhang Xiaojing knit his brows and thought it over closely, and could not help a shudder running through his frame.",
# L309
"He Zhizhang's design in arranging it so could not be plainer. Once the Son of Heaven was dead, the heir apparent could ascend the throne in full and open right. And Li Linfu, who had left midway, would of course be branded the author of the disaster and made to bear every charge.",
# L310
"He Zhizhang had never acted for his own gain, nor for the gain of his own family. All that he had schemed and toiled at was for the heir apparent.",
# L311
"'To think that Director He, this Guest of the Heir Apparent, should be more fervent even than you, a Hanlin academician in the Eastern Palace's service...' As Zhang Xiaojing said this, his tone held not resentment but a full measure of frustration. But in the next instant Li Bi's words left him stunned.",
# L312
"'No—it is not Director He.' Li Bi slowly shook his head.",
# L313
"'What? Not he? But every detail tallies...'",
# L314
"'He who profits most is suspect—and this gain need not be a gain in substance, nor need it be loyalty; it may also be filial devotion.' Li Bi answered with a bitter smile, and pointed a hand ahead. 'The true hidden hand behind it all is Director He's son, He Dong.'",
# L315
"'That adopted son?'",
# L316
"'Director He was willing to give his utmost loyalty to the heir apparent; and his son, to fulfil his father's wish to be loyal, in his own way gave his utmost filial devotion.' Li Bi's tone was full of feeling, yet he did not spell it all out.",
# L317
"Zhang Xiaojing was wholly at a loss what to say. This surmise was too outlandish for words, quite beyond the reasoning of any normal man; only the maddest of madmen would think in such a way.",
# L318
"'A man who could contrive a plan like the Que-le Huo-duo—is he not mad enough?' Li Bi retorted.",
# L319
"'What proof have you for this saying of yours?'",
# L320
"Li Bi lay in the earthen pit and slowly raised one finger: 'You said just now that, when Yuan Zai framed Feng Dalun, he put forward one proof: that the lantern-tower's bamboo passes had all been countersigned by Feng Dalun, this recorder of the Forestry and Crafts Bureau, and that this was how the aphids had slipped through. The charge is not, in itself, wrong—only the one who truly had the power to do it was not Feng Dalun the recorder, but He Dong; for his post was that of Feng Dalun's own superior, the vice-director of the Forestry and Crafts Bureau!'",
# L321
"This one detail burst all at once in Zhang Xiaojing's mind, and his breathing grew heavy at it. Put so, it did indeed explain how the aphid artisans could come and go so brazenly in the lantern-tower: with He Dong, this vice-director of the Forestry and Crafts Bureau, for their man inside, it was all too easy.",
# L322
"'And there is that grand mansion with the self-raining pavilion in Anye Ward, whose concealed buyer's identity has been in doubt all along. He Dong, as Director He's adopted son, does not enter the clan register, yet keeps his noble standing; for him to see to the formalities of the concealed purchase could not be more fitting.",
# L323
"'Director He lies gravely ill; his eldest son He Zeng is far away with the army, and his youngest is still a babe in swaddling-clothes, so that the only one who could attend the spring banquet in his stead was He Dong. Were one to look now at the guest-list of the Qinzheng Wuben Tower, his name would surely be on it. And he alone could, without turning a hair, lay down two letters at the banquet to draw out both the heir apparent Li Heng and the Right Minister Li Linfu.",
# L324
"'It may be that He Dong, knowing full well that I had laid hands on his father, yet, of all things, held it in and gave no sign, and even went along with me to Gan Shoucheng's to play out a scene of forcing the palace. By then he most likely knew already that the aphids would strike at the Jing'an Bureau, and had, in secret, laughed his cold laugh over it who knows how many times. And I, like a fool, thought I had deceived them all—the order for the aphids to kill me was, most likely, sent out straight from He Dong.'",
# L325
"Clue after clue, Li Bi had joined them all up. That one blast seemed to have parted every mist, and a filial schemer who had toiled at his design slowly rose into view. But Zhang Xiaojing could by no means picture it: that this upheaval, which had all but turned Chang'an upside down, should have been plotted, from first to last, by one wooden and dutiful son.",
# L326
"'I do not believe it. Without Director He's tacit leave and cooperation, He Dong could never have had so strong a hold on things.'",
# L327
"Zhang Xiaojing would have argued still, but Li Bi looked at him and shook his head bitterly: 'That answer we shall likely never know.'",
# L328
"'Why? Director He may lie unwaking in his swoon, but if only we seize He Dong—ah!' The words were scarcely out of Zhang Xiaojing's mouth before he grasped the answer, for Li Bi's gaze was fixed all the while on that stretch of freshly made ruin, the smoke still curling up from it.",
# L329
"'The one who stood at the gate just now was He Dong himself. To his very death, he was a dutiful son.'",
# L330
"That blast just now had been too violent by far; He Dong, standing at its very heart, must already be gone, not a bone of him left. With his filial ways, once he knew the plot laid bare, he could by no means drag his whole family down with him: death was the only choice.",
# L331
"The two clambered slowly out of the pit and, propping each other up, made their way toward the He residence, now a ruin. All along this road lay wreckage, broken rubble and shattered wood; the fair scene of a moment before had turned in an instant into the likeness of hell. He Dong's bones had crumbled to powder along with that bizarre ambition and filial devotion. And that upheaval which had shaken the whole city had, of all things, taken its rise from this very place.",
# L332
"Twelve double-hours before, they could never have thought it would come to such an end as this, nor that it would end here.",
# L333
"The two stood amid the ruins, yet knew not what they should look for, and could only stand there blankly. Before He Dong took his own life, he had surely spirited He Zhizhang away; a dutiful son could not bear the name of parricide. But even to find He Zhizhang now would be of no use. The old man was sick past cure and could not speak; whether he had known nothing at all of his adopted son's plan, or had silently given it his leave, would likely remain a mystery forever.",
# L334
"Li Bi steadied himself against the mansion gate, now but half standing, and all at once turned his head and gave a cold smile at the thin smoke in the middle air, as though speaking to a newly dead soul: 'He Dong, O He Dong, you may go now with a quiet heart. Your plot will not be made public; the innocent house of He will not be dragged down by you, but will go on enjoying Director He's glory and the shade of his bounty, and nothing will change.'",
# L335
"A fierce light shot suddenly from Zhang Xiaojing's single eye: 'Why?! So great a matter as this—how can it be dealt with so?'",
# L336
"'It is because it is so great a matter that it will be dealt with so.' Li Bi said calmly, his eyes still fixed on the thin smoke in the air. 'The kinsman of a great minister the Son of Heaven so trusts, caught up in the chaos of Chang'an? Would the court have any face left at all? Would it mean the Son of Heaven had no discernment of men?'",
# L337
"'But...'",
# L338
"'On the fifth of the first month, the Son of Heaven, with all solemnity, saw Director He off out of the city of Chang'an; he is already on the road home, not in Chang'an. This is a fact none will dare deny. So the scapegoat finally thrust forward will be, just as you say, that neither-here-nor-there Feng Dalun. As for He Dong, he will be counted one of the victims of this upheaval, blown to death by the aphids' fierce-fire thunder... heh, heh.'",
# L339
"At this Zhang Xiaojing was struck dumb.",
# L340
"Li Bi walked a few steps further into the ruins, bent to pick up a half-panel of scorched window-lattice, turned it about a while, then tossed it carelessly aside: 'A pity that, after this, the Jing'an Bureau is surely past saving, and I too shall likely be driven out of Chang'an. But be easy: I promised to pardon your capital crime, and I will assuredly do it; and if Tanqi wishes to go with you, then let her, I set her free—only it is a pity for the heir apparent, whose position hereafter will, I fear, grow harder and harder...'",
# L341
"Zhang Xiaojing straightened up and came to Li Bi's side. His shoulders were trembling, his lips shaking, and the flame of wrath he could not hold down in his eyes was near to bursting forth. Li Bi thought he meant to lay hands on him, and calmly drew up his chest. But instead Zhang Xiaojing gritted his teeth, kicked the half-panel of window-lattice flying, and all but roared out:",
# L342
"'The Son of Heaven, the heir apparent, the throne, the Jing'an Bureau, the court, interest, loyalty... is this all you people think about, the whole day long?'",
# L343
"'What else?' Li Bi cocked his head.",
# L344
"'The dwellers of this city of Chang'an are a million strong. Merely to offer up loyalty to the heir apparent, merely to render filial duty to a father—may one stake their very lives on it? Do you know how many innocent people have been caught up in this, from last night until now? What, in the end, are human lives reckoned to be worth? Why is it not these people you care for first? Why can you take such a thing so calmly?'",
# L345
"Faced with this sudden and violent questioning, Li Bi sighed helplessly. He clapped the dust from his hands and walked, swaying, to the edge of the residence. This was very nearly the highest point of the Leyou Plateau, from which one could gaze out over the whole city, the view superb.",
# L346
"Li Bi stood still, pointed toward the broad sweep of the city in the distance, his look full of meaning: 'You served nine years as a buliang chief—do you still not understand? This, this is the very nature of Chang'an.'",
# L347
"Zhang Xiaojing suddenly clenched his five fingers and with one heavy blow of the fist knocked Li Bi to the ground. The other fell amid the ruins of the He residence, blood trickling from the corner of his mouth, his face wearing a faint bitterness and self-mockery.",
# L348
"Never had Zhang Xiaojing been so angry, and never so powerless. He had long known the nature of this monster, Chang'an, yet had never truly loved it. At every moment he strove and struggled, thinking not to be devoured, and yet was always torn until his whole body was a mass of wounds.",
# L349
"All at once a few creaking sounds came from overhead. Zhang Xiaojing looked up: Li Bi's fall had set off a small tremor, and the four door-studs on the frame of the He gate, that stood for the family's standing, were tottering; then one after another they dropped to the ground, striking four deep pits into the earth.",
# L350
"Li Bi clambered up from the ground with an effort and wiped the blood from the corner of his mouth with his sleeve. That blow just now had been no light one. Yet Li Bi was not angry; his voice carried a deep weariness and a heart gone to ashes:",
# L351
"'This time I have come down into the red dust and busied myself with the affairs of the world, only to end with my Daoist heart broken. If I do not go back to the mountains and cultivate anew, I fear my attainment of the Way will be long delayed—and you? What of you?'",
# L352
"Zhang Xiaojing shook his head and did not heed the question. Limping, he made his way through the ruins of the He residence and stood at the high edge of the Leyou Plateau, looking down over the whole of Chang'an.",
# L353
"In his single eye, the hundred and eight wards were ranged, orderly and solemn, on either side of the Vermilion Bird Avenue, glittering under the shine of the sun, magnificent in their sweep. He had once heard the Hu from foreign lands say that, look the whole world over, there was no city greater or more splendid than Chang'an. Last night's clamor had left no scar upon the body of this city; it was noble and grand as ever, as though it would go on so forever.",
# L354
"A single crystal tear flowed from the long-dry socket of Zhang Xiaojing's eye—the first time in the nine years since he came to Chang'an.",
# L355
"(The End)",
]

# the source's per-chapter time-gloss (raw[355]) -> the source's own italic note.
# HOUR MATCHES: this chapter is nominally 巳初 (Snake, first half, 9 a.m.), its
# in-body dateline is 巳初, and the gloss describes 巳/9 a.m. -- all in agreement.
TIMEGLOSS = ("*[The source appends a note on the hour to each chapter:]* Nine o'clock "
             "in the morning. Si, also called ri-yu (the sun at its corner) and the like: "
             "the time drawing near to noon is called yu-zhong, the corner of noon. "
             "(Beijing time, 09:00 to 11:00.)")


def main():
    raw = open(SRC, encoding="utf-8").read().split("\n")
    src = []
    src.append(raw[1].strip() + raw[2].strip() + raw[3].strip())  # vignette (L2+L3+L4)
    src.append(raw[4].strip() + raw[5].strip())                   # dateline (L5+L6)
    for i in range(6, 355):                                       # L7 .. L355
        src.append(raw[i].strip())
    timegloss_src = raw[355].strip()                              # L356

    assert len(src) == len(BODY), \
        "paragraph count mismatch: %d source vs %d english" % (len(src), len(BODY))

    # verbatim guarantee: concatenation of all blockquotes == source content
    concat_bq = "".join(src) + timegloss_src
    concat_src = "".join(l.strip() for l in raw[1:356])           # L2 .. L356
    assert concat_bq == concat_src, "VERBATIM MISMATCH"
    print("verbatim check OK: %d source chars, %d body paragraphs"
          % (len(concat_src), len(src)))

    out = ["## H2 " + TITLE_EN, ""]
    for zh, en in zip(src, BODY):
        out.append("> " + zh)
        out.append(en)
        out.append("")
    out.append("> " + timegloss_src)
    out.append(TIMEGLOSS)
    out.append("")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
