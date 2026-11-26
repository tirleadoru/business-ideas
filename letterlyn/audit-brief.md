# LetterLyn word audit brief (paste before each pack)

You are checking one pack of a word-search game. Each topic has 16–18 English–Romanian word pairs. The player finds the Romanian word in the grid (or the English one in the other direction), so each pair must be an exact translation. Check every pair against these rules and report only real problems, each with the topic, the pair, the problem and a proposed fix.

**Allowed, do not flag:**
- 16, 17 or 18 words in a topic (all are fine).
- Topics marked "not in Learn" (e.g. Pet names): their Romanian list is its own list, not a translation.
- The same Romanian word for two different English words in different topics.
- Proper names and loanwords that Romanians really use (LABRADOR, PET SHOP, GUPPY).
- Two-word answers (they are joined in the grid, spaced in the list).

**Flag these:**
1. **Wrong or loose translation**: the Romanian means something else or something wider (NUFERI = water lilies, not lily pads). Check DEX/dexonline for spelling (DOOM forms) and meaning.
2. **Different kind of word**: noun must pair with noun, verb with verb, adjective with adjective (JOG = ALERGARE is wrong: verb vs noun).
3. **Romanian verbs in the "it does" form** (present, 3rd person, no "se"): CLIMB = CAȚĂRĂ, SNIFF = ADULMECĂ. Dog commands are commands: SIT = ȘEZI, FETCH = APORT, HEEL = LA PICIOR.
4. **Dictionary form**: adjectives masculine (TABBY = TIGRAT), except breed names agreeing with the animal (PERSANĂ). Nouns without the article (MAI, not MAIUL). Plural only when the English is plural, and both sides the same number.
5. **Same thing twice in one topic**: two pairs naming the same object, sound or action (FETCH and RETRIEVE; SQUEAL and SQUEAK; DISH and BOWL).
6. **One word inside another in the same topic**, forwards or backwards, in either language (APORT inside APORTEAZĂ, BEE inside BUMBLEBEE). Those two can't share a grid.
7. **Fit with the topic**: a word that doesn't belong to the topic's subject, or is so generic it could be anywhere.
8. **US English only**: flag UK words and spellings (COLOUR, TRAINERS for sneakers, TAP for faucet).
9. **Spelling**: ș and ț with the comma below (never ş ţ); correct diacritics.
10. **Consistency**: if you know the same English word is translated differently elsewhere in the pack, say which form is better.

**Fixes:** a fix must be a word that fits the topic. Keep in mind the grid limit: at most 14 letters (spaces don't count), and long words are harder to fit. Don't propose a fix that creates problem 5 or 6. Where people genuinely say it different ways and the current word is correct, don't flag it.

**Format:** one line per problem: `Topic · EN=RO → proposed EN=RO · reason`. End with the list of topics that have no problems.
