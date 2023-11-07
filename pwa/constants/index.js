export const TIMERANGE = {
  TODAY: 'today',
  YESTERDAY: 'yesterday',
  LAST_WEEK: 'last-week',
  LAST_MONTH: 'last-month',
}

const NEUTRAL = 'NEUTRALNO'
const LEFT = 'LIJEVO'
const RIGHT = 'DESNO'

export const SLANTS = {
  1: LEFT,
  2: NEUTRAL,
  3: RIGHT,
}

export const TERRITORIES = [
  [{ name: 'FBIH', svgIndex: 1 }],
  [{ name: 'RS', svgIndex: 2 }],
  // [{ name: 'Brčko', svgIndex: 3 }],
]

export const PARTIES = [
  { id: 1, longName: 'Narodni Evropski Savez Bosne i Hercegovine', name: 'NES BiH' },
  { id: 2, longName: 'Hrvatska stranka prava dr. Ante Starčević Bosne i Hercegovine', name: 'HSP' },
  { id: 3, longName: 'Narodni demokratski pokret', name: 'NDP' },
  { id: 4, longName: 'Građanski savez', name: 'GS' },
  { id: 5, longName: 'Srpska demokratska stranka', name: 'SDS' },
  { id: 6, longName: 'Socijalistička partija Republike Srpske', name: 'SP RS' },
  { id: 7, longName: 'Nezavisni blok', name: 'NB' },
  { id: 8, longName: 'Savez za bolju budućnoost', name: 'SBB' },
  { id: 9, longName: 'Hrvatska demokratska zajednica Bosne i Hercegovine', name: 'HDZ BiH' },
  { id: 10, longName: 'Hrvatska demokratska zajednica 1990', name: 'HDZ 1990' },
  { id: 11, longName: 'Savez Nezavisnih socijaldemokrata', name: 'SNSD' },
  { id: 12, longName: 'Demokratska fronta', name: 'DF' },
  { id: 13, longName: 'Naša stranka', name: 'NS' },
  { id: 14, longName: 'Laburistička stranka', name: 'Labur' },
  { id: 15, longName: 'Demokratski narodni savez', name: 'DNS' },
  { id: 16, longName: 'Narod i pravda', name: 'NiP' },
  { id: 17, longName: 'Socijaldemokratska partija Bosne i Hercegovine', name: 'SDP BiH' },
  { id: 18, longName: 'Stranka demokratske akcije', name: 'SDA' },
  { id: 19, longName: 'Pokret demokratske akcije BiH', name: 'PDA BiH' },
  { id: 20, longName: 'Partija demokratskog progresa', name: 'PDP' },
  { id: 21, longName: 'Ujedinjena Srpska', name: 'US' },
]
