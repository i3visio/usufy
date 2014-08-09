import logging

def generatingProfiles(nicks):
        """ 
                Iterating on the list of nicks to find '.' or "_" and replace them according to:
                        - if '.' in n: 
                                adding n.replace('.', '_')
                                adding n.replace('.', '')
                                ...
                        - if '_' in n: 
                                adding n.replace('_', '.')
                                adding n.replace('_', '')
                                ...
                Values returned:
                        a sorted list with the new nicknames.
        """

        listSeparators = ['.', '_', '-']

        aux = []
        for n in nicks:
                # Adding the current nick
                aux.append(n)

                # Initializing candidates list
                candidates = []

                # Checking if the nick contains a separator
                for curSep in listSeparators:
                        if curSep in n:
                                for newSep in listSeparators:
                                        candidate = n.replace(curSep, newSep)
                                        if candidate not in aux:
                                                aux.append(candidate)
                        # trying deleting separator
                        if curSep in n:
                                candidate = n.replace(curSep, '')
                                if candidate not in aux:
                                        aux.append(candidate)
        return sorted(aux)

