#!/usr/bin/env python3
"""
Module DB pour gérer les interactions avec la base de données.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """
    Classe DB gérant la connexion et les opérations sur la base de données.
    """

    def __init__(self) -> None:
        """
        Initialise une nouvelle instance de la base de données.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Objet session mémorisé (memoized) pour les requêtes SQLAlchemy.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Ajoute un nouvel utilisateur à la base de données.

        Args:
            email (str): L'email de l'utilisateur.
            hashed_password (str): Le mot de passe haché de l'utilisateur.

        Returns:
            User: L'objet User nouvellement créé.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Trouve le premier utilisateur correspondant aux critères de recherche.

        Args:
            **kwargs: Critères de recherche (ex: email="test@test.com").

        Returns:
            User: L'utilisateur correspondant.

        Raises:
            NoResultFound: Si aucun utilisateur n'est trouvé.
            InvalidRequestError: Si un critère ne correspond à aucune colonne.
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Met à jour un utilisateur existant dans la base de données.

        Args:
            user_id (int): L'ID de l'utilisateur à modifier.
            **kwargs: Les attributs à mettre à jour et leurs nouvelles valeurs.

        Raises:
            ValueError: Si un argument ne correspond pas à un attribut de User.
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"L'attribut {key} n'existe pas.")
            setattr(user, key, value)

        self._session.commit()
