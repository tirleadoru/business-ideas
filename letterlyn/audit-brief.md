# LetterLyn word audit brief (paste before each pack)

You are checking one pack of a word-search game. Each topic has 16–18 English–Romanian word pairs. The player finds the Romanian word in the grid (or the English one in the other direction), so each pair must be an exact translation. Check every pair against these rules and report only real problems, each with the topic, the pair, the problem and a proposed fix.

**Allowed, do not flag:**
- 16, 17 or 18 words in a topic (all are fine).
- Topics marked "not in Learn" (e.g. Pet names): their Romanian list is its own list, not a translation.
- The same Romanian word for two different English words in different topics.
- Proper names and loanwords that Romanians really use (LABRADOR, PET SHOP, GUPPY).
- TORPOARE is a dictionary word (rare, = toropeală); TORPOREALĂ does not exist.
- PRĂBUȘIRE also means a sudden decline (figurative), e.g. a population crash.
- An English uncountable noun (FRUIT, STRAW, LUGGAGE) may pair with the Romanian plural when that's how Romanian says it (FRUCTE, PAIE, BAGAJE), as long as the topic makes the meaning obvious (Fruit salad, Straw hats); FRUIT = FRUCT when it means a single fruit or fruit in general.
- GRASSHOPPER=LĂCUSTĂ and KATYDID=COSAȘ are the catalogue's standard pairs.
- PALMURĂ = the webbing between toes (frogs, water birds); it has no palm-leaf meaning.
- CÂRD for any group of animals of one kind, mammals too (DEX: «grup mare de animale sau de păsări, de pești de același fel»), e.g. HERD=CÂRD for deer.
- Two-word answers (they are joined in the grid, spaced in the list). Dashes only where the dictionary writes them (T-SHIRT, FLOAREA-SOARELUI, PEȘTE-SPADĂ); flag an invented dashed name or a dash the dictionary doesn't use.
- Pack or topic titles with "and" / "și" (fine when there isn't content for two).
- A word whose link to the topic needs explaining but is true and interesting (COLONEL in Mustaches): instead of replacing it, you may propose a short "why here" line for its word card (see Format).

**Flag these:**
1. **Wrong or loose translation**: the Romanian means something else or something wider (NUFERI = water lilies, not lily pads). Check DEX/dexonline for spelling (DOOM forms) and meaning.
2. **Different kind of word**: noun must pair with noun, verb with verb, adjective with adjective (JOG = ALERGARE is wrong: verb vs noun).
3. **Romanian verbs in the "it does" form** (present, 3rd person, no "se"): CLIMB = CAȚĂRĂ, SNIFF = ADULMECĂ. Dog commands are commands: SIT = ȘEZI, FETCH = APORT, HEEL = LA PICIOR.
4. **Dictionary form**: adjectives masculine (TABBY = TIGRAT), except breed names agreeing with the animal (PERSANĂ). Nouns without the article (MAI, not MAIUL). Plural only when the English is plural, and both sides the same number.
5. **Same thing twice in one topic**: the same word in two forms (singular and plural: VENTUZĂ and VENTUZE) or a plain duplicate of one thing (FETCH and RETRIEVE; CALF and CALVES). Synonyms are FINE and must not be flagged (CLEVER=ISTEȚ and INTELLIGENT=INTELIGENT, CALM and RELAXED): they teach two words. A verb and a noun from one root are fine too (SING=CÂNTĂ, SONG=CÂNTEC).
6. **One word inside another in the same topic**, forwards or backwards, in either language (APORT inside APORTEAZĂ, BEE inside BUMBLEBEE). Those two can't share a grid. It means one WHOLE word inside another; two words that only share a part are fine (PISICĂ NEAGRĂ and UȘIȚĂ DE PISICĂ).
7. **Fit with the topic**: a word that doesn't belong to the topic's subject, or is so generic it could be anywhere.
8. **US English only**: flag UK words and spellings (COLOUR, TRAINERS for sneakers, TAP for faucet).
9. **Spelling**: ș and ț with the comma below (never ş ţ); correct diacritics. Only Romanian letters in the Romanian word (A–Z, Ă Â Î Ș Ț): foreign letters like É or Ü are a problem (NAZARÉ → NAZARE).
10. **Consistency**: if you know the same English word is translated differently elsewhere in the pack, say which form is better.

**Fixes:** a fix must be a word that fits the topic. Keep in mind the grid limit: at most 14 letters (spaces don't count), and long words are harder to fit. Don't propose a fix that creates problem 5 or 6. Prefer single-word fixes: a puzzle holds at most 2 two-word answers in Classic and 4 in Expert, so a new two-word answer often won't fit. Our tools check every other rule (repeats across puzzles, grid fit), so it's fine to propose a few alternatives in order of preference. Where people genuinely say it different ways and the current word is correct, don't flag it.

Any "why here" line you propose is our own explanation: never mention DEX, DOOM or a dictionary in it.

**Format:** one line per problem: `Topic · EN=RO → proposed EN=RO (or alternatives: A=B / C=D) · reason`. For a word to keep with an explanation: `Topic · EN=RO → keep, why here: <one short line in English> / <in Romanian>`. End with the list of topics that have no problems.
