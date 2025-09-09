class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        opciones = ["piedra", "papel", "tijera"]
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        if jugador1 == jugador2:
            return "empate"
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "tijera" and jugador2 == "papel") or \
           (jugador1 == "papel" and jugador2 == "piedra"):
            return "jugador1"
        return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        if intento > numero_secreto:
            return "muy alto"
        return "muy bajo"
    
    def ta_te_ti_ganador(self):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
          # Test victoria en fila
        tablero_fila1 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila1) == "X"
        
        tablero_fila2 = [[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila2) == "O"
        
        tablero_fila3 = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_fila3) == "X"
        
        # Test victoria en columna
        tablero_col1 = [["X", "O", "O"], ["X", "O", "X"], ["X", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col1) == "X"
        
        tablero_col2 = [["X", "O", "X"], [" ", "O", "X"], ["X", "O", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col2) == "O"
        
        tablero_col3 = [["X", "O", "O"], ["X", "X", "O"], [" ", " ", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_col3) == "O"
        
        # Test victoria en diagonal principal
        tablero_diag1 = [["X", "O", "O"], ["O", "X", "O"], ["X", "O", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag1) == "X"
        
        # Test victoria en diagonal secundaria
        tablero_diag2 = [["X", "O", "O"], ["X", "O", "X"], ["O", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag2) == "O"
        
        # Test empate (tablero lleno sin ganador)
        tablero_empate = [["X", "O", "X"], ["O", "O", "X"], ["O", "X", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_empate) == "empate"
        
        # Test juego continúa (tablero incompleto sin ganador)
        tablero_continua = [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_continua) == "continua"
        
        # Test tablero vacío
        tablero_vacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_vacio) == "continua"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        import random
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        if desde_fila == hasta_fila:  # horizontal
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False
        if desde_col== hasta_col:  # vertical
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False
        return True