#!/usr/bin/env python3
"""Chapter 9 body trim: paragraphs 1-267 of chapters/Chapter_09.md.

REPL[idx] = new full paragraph text
DEL[idx]  = list of exact phrases to remove from that paragraph

Paragraph count is unchanged, so the coda indices (268+) stay valid for the
follow-up coda script.
"""
import io
import sys

PATH = "chapters/Chapter_09.md"

REPL = {
    1: "The practice staff cracked overhead, hard enough to sound like a snapped mast. In the alcove, the salve smelled of crushed mint and something older underneath, a bitter root Iroh bought by the jar and never named. Jake kept his eyes on the lamp.",
    16: "Overhead the deck thudded. Not the dull tramp of boots going about their work, but a heavier, ragged beat, one set of feet driving and another falling back. A sharp, flat crack came under it, then another, and Jake's hands went still in Iroh's.",
    20: "The deck was gray and wet and smelled of soot. Two days of scrubbing had not lifted the black from the aft rails, and the stern still listed, a slow lean to port. A thin brown smoke leaked from the stack, thinner than it had been, but wrong in color. The crew kept to the middle of the ship with their heads down, coiling line that did not need coiling, giving the center of the deck a wide berth.",
    22: "He had stripped to his undershirt despite the cold. Strips of linen circled both his wrists, Iroh's work, the knots small and tight. He was driving Lieutenant Jee across the planks with a practice staff, and there was no form in it. Jee was a competent fighter, but he was backing up now, staff held in front of his chest like a door, and every time he found his footing Zuko took it from him. Zuko did not pause or reset. He just came again, breath ragged, hair stuck to his forehead, the scar gone dark with sweat on the ruined side of his face.",
    24: "*If he stops, he has to think about the sky over the island,* Jake thought. *The ground-fire. The line firing with no signal.* He put it away where he put most things, and looked at the practical problem: Jee's left foot was dragging, and the older man was breathing through his mouth.",
    39: "It was not the engine. Jake knew every note of the engine by now. This was something else, the whole hull rolling against its own list as the bow swung. A coil of rope slid across the planks and fetched up against the rail. Overhead the rigging sang one long note as the wind shifted.",
    46: "He had come up the stair behind Jake at his own pace. He stood at the edge of the cleared space with his hands folded over his stomach, wearing an expression of such gentle, regretful dignity that Jake felt the crew's collective breath go out.",
    53: "\"The white lotus. From my Pai Sho set. It is a rare piece, and a set without it is very nearly no set at all.\" Iroh sighed. \"I have turned my quarters upside down. It is gone. The nearest Earth Kingdom port is half a day's sail from here, and the markets there are reputed to be good.\"",
    58: "It was not a bolt. It was a roar of fire and black smoke that struck the planks of the overhead and flattened out against them. Heat washed over the deck, and a deckhand ducked. The smell of scorched pitch came down thick and bitter. The cloud rolled under the bridge and thinned out over the rail, and when it was gone Zuko stood with his chest heaving, scorch marks climbing the boards above him in a black fan.",
    63: "Iroh was not looking at him. He was watching the prince's back go forward along the rail, and his face, now that Zuko could not see it, was not the face of a man who had lost a game piece. It was tired, and very patient. Jake understood then that there was no tile. There were ten minutes on land, and an old man who thought Zuko would die of the running if somebody did not make him stop.",
    64: "It was dangerous. Any port was dangerous, with Zhao hunting them and a bounty that might be posted by now. He thought it as he went to the rail to look at the coast coming up gray and green through the haze.",
    66: "The ship limped toward the harbor on its stuttering engines, and by midday the first masts were showing above the water. Jake went back down to the alcove for the gloves. They were still stiff, and it took him a long time to work his hands into them.",
    68: "The smell reached them before the gangplank did. Fish and tar, crushed ginger, the sweet rot of fruit left too long in the sun. Overhead the gulls screamed at the fishwives, and under that rose the market itself, a dozen sellers at once, each pitching a voice over the others.",
    70: "The coat was buttoned to the throat. Under it he wore a plain brown tunic borrowed from the stores, and nobody had asked him why his own red crew jacket was rolled at the bottom of a sea chest. A good port was a port where nobody looked twice at a boy of his height. He walked a half-step behind Zuko's left shoulder, where he could see most of the street and most of the prince's face.",
    71: "Two men in dull gray stood by a fruit stall with spears on their shoulders. Earth Kingdom, local garrison, bored. Jake marked them and let his eyes pass on. A third man leaned against a post eating roasted nuts, with a sword on his hip and the wrong kind of stillness, and Jake held on him longer.",
    74: "He had stopped at a stall hung with brass and bamboo and string. Iroh leaned over a tray of carved game pieces, picked up one after another, held each to the light, and set them down again with great courtesy.",
    80: "The woman selling the pieces showed Iroh a white blossom carved from bone. He turned it over twice and shook his head. It was a lotus, but a poor one, with the petals too thick and flattened. Zuko stood with his arms folded and watched the minutes go by, and Jake watched him do it.",
    81: "The prince had put a hood up. It shadowed the scar without hiding it. His wrists were still bound in Iroh's linen, and when he held his arms folded the knots showed at his cuffs. Jake thought *keep them covered*, and did not say it, because saying it would only have turned Zuko's attention on the hands beneath them. Not today.",
    82: "By the third stall Iroh had gathered a tsungi horn, which he tucked under one arm like a prize. By the fifth he had added a small stone monkey with its paws clasped over its ears. By the seventh he had stopped asking about the tile at all and was haggling over tin bells.",
    88: "Jake looked at the carved monkey, at its stone paws and its small, smug face. Zuko did not look at the monkey. He looked at Iroh, and then at the street, and Jake saw the exact moment the prince decided to stop arguing, because his shoulders lowered a fraction and went hard.",
    89: "They had come out at the water end of the market, where the stalls gave way to barrels and the smell of fish thickened. Rough tables had been dragged up against a warehouse wall under a patched canvas awning. Three or four men sat around one with tankards. They were not Earth Kingdom garrison and not fishermen, though they had the red hands and sea-bleached eyes of both. One was thin and loud, a long-faced man in a striped vest. Across from him sat a man twice his width in a captain's coat gone green at the seams.",
    90: "Jake looked at their belts first. Short swords, a boarding axe, a coil of chain on the bench by the big man's boot. A pirate crew, or near enough to one. Six that he could see, and the awning might be hiding more. He counted the distance between the table and Zuko's back. Twelve paces. Then he closed his fingers inside his pockets and saw how much grip was left.",
    95: "Jake felt it before he understood it. It was a cold, small, exact spike under the breastbone. *Water Tribe.* He had heard those words in a dozen voices over three years. Always in the past tense. Always about somebody else. A girl. The torn ribbon lay in Zuko's pocket, the pale stone against the dark blue, and Jake did not look at the prince's pocket. He looked at the pirates' hands.",
    98: "He did not walk to the table so much as arrive at it. One moment he stood beside his uncle, hooded and silent, and the next he was three paces from the pirates with his shoulders squared and his weight forward. In the same movement he had stepped a half-pace to the right, so that his body was between the table and the place where Jake stood. He did not think the prince knew he had done it.",
    103: "For a moment nobody answered. Jake's gaze moved across the table: the thin man's right hand drifting toward his belt, the captain's left sliding down by the chain. He took a half-step forward to stand level with Zuko's shoulder, not behind it, and kept his hands where the pirates could see them. They were in his pockets. It would have to do.",
    112: "Zuko's jaw shifted. Jake saw him weigh it. The hunger in the set of his face was too sharp, and the thing the pirates were offering was exactly the shape of the hole the Avatar had left in the sky.",
    122: "The big pirate in the captain's coat led. The thin one trotted at his elbow, and a third came behind with a coil of rope over his shoulder. Zuko walked in the middle of them like a man who had not decided whether he was among allies. Jake took the rear of Zuko's flank, with the three soldiers fanned out behind him in the brush, his hands loose at his sides.",
    123: "The captain's price had come out on the way, in pieces. The girl had a scroll. A real one, the captain said, waterbending, old and worth a fortune. The pirates had held it for a night before she took it back. They wanted it, and Zuko had said they could have it. Jake had watched him say it, with no change in his face at all.",
    129: "She was about his own age, perhaps a little younger. She wore a heavy parka of blue, dyed deep, with white fur at the collar and cuffs and a pale pattern stitched down the front in thick knotwork. Her hair was dark and fell past her shoulders in a long braid. Her skin was a warm brown, and her boots were fur-lined too, absurdly heavy for this weather. She had pushed her sleeves back to the elbow.",
    131: "Jake had seen waterbending on Kyoshi Island and in the cold dark moment when a girl in blue had stopped a dozen soldiers in place with a gesture. He had never seen it done simply, for its own sake, by someone who thought she was alone. The girl raised her arms, and water climbed out of the pool in a long clear rope. She turned her hands over, and the rope turned with her. It was careful and not yet certain. When it faltered she scowled and began again. The water swung out and around and back, and the movements came from her hips and her shoulders, wide and rolling, her whole body leaning into the pull and then giving it back.",
    133: "*Southern.* He had her clothes, the stitching, the cut of the fur. She had come from the same ice he had come from. The thought did not warm him, and he waited for it to. He looked at her brown face and her bent shoulders and thought, with a flat, hollow wonder, *this is my blood*, and waited for the part that was supposed to follow.",
    134: "Nothing came. He looked at the pattern down the front of her parka and had no idea what it meant. Was it a family mark, or a tribe's? She wore it like skin. He knelt in the ferns in a coat that smelled of ship's coal, with Fire Nation drill in every muscle of his back, and understood that he was the one in costume.",
    136: "The pirates moved first. The thin one broke from the ferns with a shout, and the girl spun toward it, and the water in the air lashed out in a blue crack that caught him across the chest and flung him backward into a bush. The captain laughed, and two more were on her before she could turn again. Zuko came down the bank in three strides, and a soldier cut around the other side of the pool. Jake slid out from the roots and took the high ground at the lip of the hollow. The girl got a second whip of water out, and then someone caught her wrists from behind, and the water dropped from the air in a heavy splash.",
    137: "It took four of them to move her. She fought the whole way, kicking, twisting, shouting in a high, furious voice that had no fear in it at all. Zuko took a rope from a soldier and went around the nearest tree with her back against it. He wound the line three times about her arms and waist. When he drew the knot tight she hissed at him, and he did not look away.",
    147: "He drew out the necklace. The blue ribbon hung from his fingers with the pale stone swinging at the end. Jake had last seen it in a village by the ice, in the first week, on the neck of this girl or someone just like her. It looked small. It looked very much like what it was.",
    153: "He did not decide to. His eyes simply went down to the damp earth, and to the toes of his boots, where a crushed fern lay in the mud. He had no right to the grief that stood in the hollow, and he knew exactly how it was being used. The prince was doing this the way he did everything, head-on and with all of himself, as if the world had left him no other road. Jake had watched him do worse.",
    158: "The pirate captain had come up with his thumbs hooked in his belt. The captain nodded at a flat rock near the pool, where a long case of old yellow parchment lay half unrolled. Painted figures ran down it in a faded brush hand. Jake saw a woman with her arms raised and a ribbon of water running between her palms.",
    173: "Their ship lay against a rotten jetty at the water's edge, a low, ugly vessel with patched sails furled and a rail the color of old teeth. Zuko's launch had been dragged up the bank beside it. Jake had seen the bank on the way up and judged it by habit: two exits, one slope, a single stand of reeds. The water ran a body-length from his boots.",
    177: "There were two. The first was a boy of about Jake's own age, lean and long-limbed, in blue Water Tribe furs cut very much like the girl's. His head was shaved at the sides, the rest drawn back in a short tail. Another pirate carried a bent boomerang of dark wood at his belt like a trophy. Jake knew the boy. He had seen him on the back of the bison at Kyoshi, a white-furred shape growing smaller against the sunset, and the memory arrived whole and uninvited.",
    179: "He came last, bound at the wrists with a rope that was too thick for him. Bare feet, loose orange and yellow cloth, a bruise darkening on one cheek. His head was shaved clean, and on it, running to a point between his eyebrows and in two lines along his hands, was the blue arrow. Jake looked at the small, solemn face and thought *him* at once. The boy who had stood in a doorway and been, for an instant, the whole sky.",
    190: "There was a pause that Jake would have liked to measure. The captain's eyes slid from the scroll in Zuko's fist to the child in orange. Behind the captain, the thin pirate was grinning like a man who had been shown a bigger purse.",
    193: "It was only a small movement, but Jake felt it in the back of his own neck. The ground-fire air of the bridge came over the shore. He took his hands out of his coat.",
    197: "Somewhere in the confusion a pirate flung something small and round against a stone. It cracked, and gray smoke billowed outward. A second went off, then a third. Within a few breaths the shingle had vanished into a stinging fog that tasted of sulfur. Jake lost the ship. He lost the jetty. He found Zuko by the sound of him, the dull crackle of fire flung into smoke, and stepped into the gap at the prince's back. Their shoulders met, and held.",
    199: "\"Right,\" Zuko said, short and low. A pirate lunged out of the haze on that side, and a ribbon of flame took the man's blade at the hilt. Jake turned his shoulder a hand's breadth and was already facing the next, a stocky pirate with a hooked cutlass. Jake did not draw the knife. He let the man come in, side-stepped the first cut, and caught the second on his forearm. He kept his feet.",
    205: "Pain came up his arms in a white sheet, and he kept his hands open. The left one would not close all the way, so he did not ask it to. When a second pirate rushed him, he turned his forearm into the man's guard and stepped inside, whipped a thin lash of water across his knees, and watched the legs go out from under him. Another burst. Another half-step. Pressure, release, reposition. The river spun about him in quick tight coils, never longer than he needed. Zuko's fire flared and died on his other side. A pirate yelled. A shape fell. For a handful of heartbeats the shore was only the two of them, back to back, a wall with no gap.",
    208: "She had cut herself free. There was still a length of rope hanging off her left wrist. The water had come up off the deck in a thin hard line and gone through it while every man on the shore was looking somewhere else. The boy with the shaved sides was beside her, the boomerang back in his fist. She stood with her feet planted wide and her arms thrown out in front of her. Under the keel the river gathered itself and heaved, a great smooth swell of water pushing the heavy hull out into the channel. It was the same long rolling motion he had watched in the woods, only vast now, her whole body leaning into the push and giving it back.",
    221: "Nobody answered. The little launch swung out from the bank, its stolen crew hauling at the oars, and set off down the river after the pirate ship. They drew out into the middle of the stream and diminished together into the gray, two shapes in a line. Far below, a long, low sound had begun to rise above the water, a low continuous roar that Jake had been hearing for some time without knowing it.",
    224: "Jake had not noticed he was still bending until the last of it slid off his hands. It came away from the gloves in a long dull trickle, and the strain went with it. His knees told him first. Then the arms, then the hands, hot and swollen and beating like second hearts.",
    226: "The shore had been scraped raw. A long burnt scar ran across the shingle where Zuko's fire had struck the wet stones. Only a heavy sword remained, buried to the hilt where it had missed the prince. Jake looked at it. He did not touch it.",
    230: "Jake could see him where the bank rose into a spur of bare gray rock above the lip, a dark shape against the shine, with one arm stretched toward the water as though he could close his fist around the current. The soldiers had stopped well short of him. Nobody was going to stand next to the prince just now.",
    236: "He would have missed it if he had been looking anywhere else. It was white against the pale sky, vast and slow. It lifted out of the haze, higher than the treetops and then higher than the spray. As it banked away along the cliff he saw small shapes huddled on the broad back. One of them, very small, was standing up to wave.",
    240: "Iroh had come up the slope. He walked with his hands tucked into the sleeves of his robe. He stopped beside Jake, looked down at the broken launch, and nodded a little sadly, as though acknowledging a friend.",
    243: "\"Oh, but I think you will.\" Iroh drew one hand from his sleeve and then the other. He reached into the left sleeve and brought out a small white tile. \"That lotus tile,\" he said, \"was in my sleeve the whole time!\"",
    246: "Zuko crossed the rock in three strides. He snatched the tile from Iroh's fingers, his hand shaking so badly that the little white flower trembled. Then he turned, drew back his arm, and hurled it out over the edge with everything he had.",
    249: "\"It's *your* tile.\" Zuko's voice came raw out of his chest. \"We've lost the boat and the pirates and the—\" He stopped. Then he turned from the edge and walked off the rock, down the slope toward the trees.",
    250: "He passed Jake without a glance. Jake had known he would. Zuko had looked straight through him at the trees. He had not seen. Whatever had happened in the smoke between a boy on the shore and a girl at a rail, it had passed Zuko by entirely, and Jake did not know yet whether that was luck or something worse.",
    251: "Iroh stayed where he was. He was looking at Jake.",
    252: "It was a short look. It took in the wet coat and the torn left glove. Iroh's face did not change. But Jake saw the eyes go to the river, then to the bend, then to the empty sky over the gorge, and then come back to him, and he understood that Iroh had been standing on the slope for the whole of the fight.",
    257: "He worked it through slowly. The girl had seen him, and the girl would tell. She would tell the boy with the shaved sides, and they would put it together the way people did. A waterbender, in a Fire Nation coat, standing at the prince's back. That was the whole of what they knew, and it was enough.",
    260: "Zhao, who had stood on the dock at Ketu Harbor and sneered at a *disgraced servant boy* and thought him nothing. Zhao, with his fleet across the border waters, was out there now searching the same woods and the same coast. When a man like that was taken he talked, or his friends did, or someone was made to. *The prince has a waterbender.* Zhao would hear it. He would stop and think. Then he would remember the thin boy on the dock who had said nothing at all.",
    261: "And everything Iroh had built since the Agni Kai, *servant* and not *bender*, *burned boy* and not *threat*, would come down at once.",
}

DEL = {
    3: [" Iroh stopped, wet the cloth from a cup of warm water, and waited for it to loosen. He did not hurry.",
        " Somewhere aft the engines ground along in an uneven rhythm, a stutter and a drag, and the sound came up through the plates and into Jake's teeth."],
    4: [" The edges were swollen and shiny, and the old scar tissue had torn along its own seam where the rope had taken his weight over the fissure.",
        "sometime"],
    11: ["Jake had been avoiding the sight of them. ",
         " Next to them lay a strip of clean linen as long as his arm, and on the shelf above the cot, folded small, the second set of wraps Iroh had cut for tomorrow. He had planned ahead for it.",
         " He expected Jake's hands to need the same attention tomorrow, and the day after."],
    18: [" Jake watched the ceiling."],
    28: [" without hurrying", " He did not look at Zuko."],
    34: ["the bright impatient waiting of a man who has been interrupted and has not decided what to do about it"],
    56: [" and the muscles of his arms drew tight beneath the wrapped wrists"],
    67: [" and the tide had eaten the bottom half of it"],
    72: [" Jake did not turn around. He hoped no one else did either."],
    76: [" Zuko did not raise his voice. He did not have to."],
    86: [" each word bitten off at the end"],
    92: [", and the whole table seemed to lean in to hear him"],
    96: [" That was the problem in front of him, and he held it with both hands because his hands could hold nothing else."],
    100: [" took his time, set his tankard down, and"],
    102: [", flat and fast, his hand coming out of the cloak and closing on the edge of the table"],
    108: [", and he did not seem to mind being shouted at"],
    114: [" The captain jerked his chin toward the tree line beyond the warehouses."],
    117: [" He never asked."],
    120: [" Behind him the soldiers were already moving."],
    125: [" a long steady rush behind the leaves and, closer, something quicker and lighter that did not belong to a river"],
    128: [", a few yards off,"],
    138: [" The salve smell had gone, and the river smell had taken over, damp and green."],
    139: [" with something at his belt"],
    143: [" He filed it with the rest."],
    144: [", and you're a bully,"],
    149: [" and for the first time since the ambush she had no words ready"],
    151: [", and then a little farther"],
    162: [" and lifted it clear of the stone"],
    164: [" Jake could smell the paper warming."],
    165: [" \"Search the woods for the boy and meet back here.\""],
    168: [" The river went on running, indifferent behind the trees."],
    169: [" He watched Zuko's flame, and the girl's hands, and the tree."],
    171: [", rough and triumphant and loud"],
    174: [" She walked with her chin up and said nothing."],
    181: [" A muscle moved in his cheek, and he stopped moving at all."],
    186: [" He had craned his neck around the pirate gripping his arms."],
    189: [" I'd say it's not even close."],
    196: [" and the two of them went down in the mud together"],
    207: [" in a long ragged rip"],
    218: [", in a voice of mild interest"],
    219: [" and Jake saw what was about to happen a moment before the captain did",
          " drawn up on the shingle,"],
    227: [" He knew without looking why the cloth stuck to him."],
    228: [" and the tops of trees growing out of a great distance below"],
    232: [" and from the rock he could see everything", ", a long way down,"],
    235: [" along the edge of the falls, in the spray, in the pool,"],
    238: [" His arms had come slowly down to his sides."],
    244: [" a slip of polished bone with a flower carved on it,"],
    245: [" and then at the pool and then at his own hands,"],
    253: [", the sort a man gives to a closed door,"],
    255: [" and found he could not make himself leave it"],
    258: [" They had looked at him and seen a stranger, and a stranger could be forgiven for what he was."],
    263: [" Under the leather the linen had held."],
    264: [" That was the thing to hold on to."],
    266: [" one tall and angry and one broad and slow"],
}

# Exact-phrase substitutions (old -> new), applied after REPL/DEL.
SUB = {
    44: [(" I want to know the name of every man on that bridge—", " I want the name of every man on that bridge—")],
    165: [(" You will go into those woods and find him, and you will bring him back to me.",
           " Go into those woods and find him, and bring him back to me.")],
    175: [(" The old man stood with the tsungi horn tucked under one arm, peacefully watching the river, and when Zuko passed him he only inclined his head.",
           " The old man stood with the tsungi horn tucked under one arm, and when Zuko passed him he only inclined his head.")],
}


def main():
    text = io.open(PATH, encoding="utf-8").read()
    ps = text.split("\n\n")
    before = len(text.split())

    for idx, new in REPL.items():
        ps[idx] = new
    for idx, phrases in DEL.items():
        for ph in phrases:
            if ph not in ps[idx]:
                sys.exit("DEL %d: phrase not found: %r" % (idx, ph))
            ps[idx] = ps[idx].replace(ph, "", 1)
    for idx, pairs in SUB.items():
        for old, new in pairs:
            if old not in ps[idx]:
                sys.exit("SUB %d: phrase not found: %r" % (idx, old))
            ps[idx] = ps[idx].replace(old, new, 1)

    out = "\n\n".join(ps)
    io.open(PATH, "w", encoding="utf-8").write(out)
    print("words %d -> %d" % (before, len(out.split())))


if __name__ == "__main__":
    main()
