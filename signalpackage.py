import numpy as np
import matplotlib.pyplot as plt

class SignalImpulse:

    def __init__(self, values=0, dt=0.001, T = 10, t0=0):

        self.T = T
        self.values = values
        self.max_T = self._define_max_T(T)
        self.dt = dt
        self.t = np.linspace(-self.max_T,self.max_T,int(1/dt), endpoint=False)
        self.t0 = t0
    
    def _define_max_T(self, T):
        
        if T <= 10:
            return 10
        else:
            return 100

    def show_values(self):

        myfig = plt.figure(figsize=(10,4))
        plt.plot(self.t, self.values)
        plt.title(self.to_string())
        return myfig
    
    def show_convolution(self, in2: 'SignalImpulse'):
        
        convolved = np.convolve(self.values, in2.values, mode="full")
        # Normalize convolution 
        amp_max = np.max(self.values) * np.max(in2.values)
        convolved = amp_max*convolved / np.max(np.abs(convolved))
 
        # New time vector will be amplified
        t_conv = np.linspace(-2*self.max_T, 2*self.max_T, len(convolved), endpoint=False)
            
        myfig = plt.figure(figsize=(10, 4))
        plt.plot(t_conv, convolved)
        plt.title("Convolution")
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Amplitud')
        plt.xlim(-20, 20)  # Establecer los límites del eje x de -20 a 20
        plt.xticks(range(-20,21, 2))
        return myfig

    def to_string(self):
        return "Custom Signal"

class unitImpulse(SignalImpulse):

    def __init__(self, A, t0):
        super().__init__(t0 = t0)
        self.values = np.ones_like(self.t)
        self.values = np.where(np.isclose(self.t, t0, atol=0.006), A, 0)
   
    def to_string(self) -> str:
        return "Delta Pulse"
        

class SquareImpulse(SignalImpulse):

    def __init__(self, A, t0, T):  
        """
        Unit square impulse with custom amplitude.

        Parameters
        ----------
        A : int/float
        Constant amplitude of the square.
        t0 : int/float
        Where the pulse will be centered.
        T : int/float
        Total width of the pulse. 

        The square will have value of A when abs(t) <= abs(t-T/2).
        """  
        # Generar el pulso rectangular
        super().__init__(T = T, t0 = t0)
        self.values = np.ones_like(self.t)
        bound1 = t0 - (T/2)
        bound2 = t0 + (T/2)
        self.values = np.where((self.t >= bound1) & (self.t <= bound2), A, 0)
        
    def to_string(self) -> str:
        return "Square Pulse"

class TriangleImpulse(SignalImpulse):
    def __init__(self, A, t0, T):
        super().__init__(T = T, t0 = t0)
        """
        Unit triangle impulse with custom amplitude.

        Parameters
        ----------
        A : int/float
        Constant amplitude of the square.
        t0 : int/float
        Where the pulse will be centered.
        T : int/float
        Width of the pulse.
        
        The triangle will have value of the equation describing the slope when abs(t) <= abs(t-T)
        """ 
        self.A = A
        self.values = self._generate_values()

    def _generate_values(self):
        values = np.zeros_like(self.t)
        for i,t in enumerate(self.t):
            if t>= self.t0 - self.T and t<= self.t0 + self.T:
                values[i] = self.A * (1 - abs((t - self.t0) / (self.T)))
        return values
    
    def to_string(self) -> str:
        return "Triangular Pulse"
