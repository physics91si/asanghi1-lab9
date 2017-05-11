# Physics 91SI
# Spring 2017
# Lab 8
#!/anaconda/bin/python
import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity.
    Inputs:
     Position-a second dimensional array that sets the initial position of the particle 
    M-the mass of the particle in grams
    """
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))
    
class Molecule:
    
    def __init__(self,p1,p2,k,L0):
        self.p1pos=p1.pos
        self.p2pos=p2.pos
        self.k=k
        self.Lo=L0

    def get_displ(self):
        return (self.p2pos- self.p1pos)
    
    def get_force(self):
        """finds the force on the two particles on a spring
        inputs: none
        Output: spring force on the two particles in the molecule. """
        initialVector=(self.p2pos[0]-self.p1pos[0])**2 + (self.p2pos[1]-self.p1pos[1])**2
        initialDisplacement=np.sqrt(initialVector)
        displacement=self.Lo-initialDisplacement
        force=self.k* initialDisplacement
        displ=self.get_displ()
        print(displ[0])
        return [(force * displ[0]/initialDisplacement),(force *displ[1]/initialDisplacement)]

        
