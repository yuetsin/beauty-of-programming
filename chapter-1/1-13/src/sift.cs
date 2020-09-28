static bool nim(int x, int y) {
    // special case
    if (x == y) {
        return true; // I win
    }

    // swap the number
    if (x > y) {
        int t = x; x = y; y = t;
    }

    // basic cases
    if (x == 1 && y == 2) {
        return false;
    }

    ArrayList al = new ArrayList();

    al.Add(2);
    int n = 1;
    int delta = 1;
    int addition = 0;

    while (x > n) {
        // find the next n
        while(al.IndexOf(++n) != -1);

        delta++;
        al.Add(n + delta);

        addition++;

        if (al.Count > 2 && addition > 100) {
            ShrinkArray(al, n);
            addition = 0;
        }
    }

    
    // Buggy! there should be x != y - n + 1.
    if ((x != n) || (al.IndexOf(y) == -1)) {
        return true; // I win
    } else {
        return false; // I lose
    }
}

static void ShrinkArray(ArrayList al, int n) {
    for(int i = 0; i < al.Count; i++) {
        if ((int)al[i] > n) {
            al.RemoveRange(0, i);
            return;
        }
    }
}