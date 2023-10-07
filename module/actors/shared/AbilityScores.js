export const baseAbilityScoreBlock = {
    STR: 5,
    DEX: 5,
    CON: 5,
    INT: 5,
    WIS: 5,
    CHA: 5,
};
export function getModifier(attr) {
    if (attr == 1) {
        return -4;
    }
    else if (attr <= 3) {
        return -3;
    }
    else if (attr <= 5) {
        return -2;
    }
    else if (attr <= 8) {
        return -1;
    }
    else if (attr <= 12) {
        return 0;
    }
    else if (attr <= 15) {
        return 1;
    }
    else if (attr <= 17) {
        return 2;
    }
    else if (attr <= 19) {
        return 3;
    }
    else {
        return 4;
    }
}
